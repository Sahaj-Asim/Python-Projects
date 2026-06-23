
# Air Quality Analysis Project
# Beginner-friendly version

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Loading dataset...")

# Load dataset
df = pd.read_csv("city_hour.csv")

# ----------------------------
# Basic Data Audit
# ----------------------------

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

# ----------------------------
# Data Cleaning
# ----------------------------

# Convert datetime column
df["Datetime"] = pd.to_datetime(df["Datetime"])

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing AQI values with median
df["AQI"] = df["AQI"].fillna(df["AQI"].median())

# Drop rows where datetime is missing
df = df.dropna(subset=["Datetime"])

# Save cleaned dataset
df.to_csv("cleaned_air_quality.csv", index=False)

print("\nCleaned dataset saved!")

# ----------------------------
# Feature Engineering
# ----------------------------

df["Hour"] = df["Datetime"].dt.hour
df["Month"] = df["Datetime"].dt.month
df["Weekday"] = df["Datetime"].dt.day_name()

# ----------------------------
# Aggregations
# ----------------------------

monthly_aqi = df.groupby("Month")["AQI"].mean()

hourly_aqi = df.groupby("Hour")["AQI"].mean()

weekday_aqi = df.groupby("Weekday")["AQI"].mean()

# ----------------------------
# Chart 1
# Monthly AQI Trend
# ----------------------------

plt.figure(figsize=(8,5))
monthly_aqi.plot()
plt.title("Average AQI by Month")
plt.xlabel("Month")
plt.ylabel("Average AQI")
plt.grid(True)
plt.savefig("monthly_trend.png")
plt.show()

# ----------------------------
# Chart 2
# Worst Months
# ----------------------------

worst_months = monthly_aqi.sort_values(ascending=False)

plt.figure(figsize=(8,5))
worst_months.plot(kind="bar")
plt.title("Worst Pollution Months")
plt.xlabel("Month")
plt.ylabel("Average AQI")
plt.savefig("worst_months.png")
plt.show()

# ----------------------------
# Chart 3
# Hourly Pollution
# ----------------------------

plt.figure(figsize=(8,5))
hourly_aqi.plot(kind="bar")
plt.title("Average AQI by Hour")
plt.xlabel("Hour")
plt.ylabel("AQI")
plt.savefig("hourly_pollution.png")
plt.show()

# ----------------------------
# Chart 4
# Weekday Pollution
# ----------------------------

plt.figure(figsize=(8,5))
weekday_aqi.plot(kind="bar")
plt.title("Average AQI by Weekday")
plt.xlabel("Weekday")
plt.ylabel("AQI")
plt.savefig("weekday_pollution.png")
plt.show()

# ----------------------------
# Heatmap Style Grid
# ----------------------------

pivot_table = df.pivot_table(
    values="AQI",
    index="Weekday",
    columns="Hour",
    aggfunc="mean"
)

plt.figure(figsize=(12,6))
plt.imshow(pivot_table, aspect="auto")
plt.colorbar(label="AQI")

plt.xticks(range(len(pivot_table.columns)), pivot_table.columns)
plt.yticks(range(len(pivot_table.index)), pivot_table.index)

plt.title("AQI Heatmap (Weekday vs Hour)")
plt.xlabel("Hour")
plt.ylabel("Weekday")

plt.savefig("aqi_heatmap.png")
plt.show()

# ----------------------------
# Findings
# ----------------------------

worst_month = monthly_aqi.idxmax()
worst_hour = hourly_aqi.idxmax()

print("\n========== FINDINGS ==========")
print("Worst Month:", worst_month)
print("Worst Hour:", worst_hour)
print("Highest Average AQI:", round(monthly_aqi.max(), 2))

print("\nPossible Reason:")
print("Traffic, industrial emissions, and weather conditions")
print("may contribute to higher AQI during these periods.")

