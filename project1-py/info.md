# Air Quality Analysis Project

## Project Overview

This project analyzes air quality data collected from a city over a period of time. The goal is to clean the raw dataset, identify pollution patterns, and create visualizations that help understand when air quality is at its worst.

The project uses Python and basic data analysis libraries to perform cleaning, aggregation, and visualization tasks.

---

## Problem Statement

Air quality datasets often contain:

* Missing values
* Duplicate records
* Inconsistent formatting
* Large amounts of hourly sensor data

This project cleans the data and answers questions such as:

* Which month has the highest pollution?
* Which hours of the day are most polluted?
* Which weekdays experience poor air quality?
* What overall trends can be observed?

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib

---

## Dataset Used

The project uses:

* `city_hour.csv`

This dataset contains hourly air quality readings.

---

## Project Workflow

### 1. Load Dataset

The CSV file is loaded into a Pandas DataFrame.

### 2. Data Cleaning

The following cleaning operations are performed:

* Convert datetime column into proper datetime format
* Remove duplicate records
* Handle missing AQI values
* Remove invalid records

### 3. Feature Engineering

Additional columns are created:

* Hour
* Month
* Weekday

These columns help analyze pollution trends.

### 4. Data Aggregation

Average AQI values are calculated by:

* Month
* Hour
* Weekday

### 5. Visualization

The project generates:

1. Monthly AQI Trend
2. Worst Pollution Months
3. Hourly Pollution Levels
4. Weekday Pollution Levels
5. AQI Heatmap (Weekday vs Hour)

All charts are saved as PNG files.

### 6. Findings

The program automatically identifies:

* Most polluted month
* Most polluted hour
* Highest average AQI

---

## Output Files

After execution, the following files are generated:

* `cleaned_air_quality.csv`
* `monthly_trend.png`
* `worst_months.png`
* `hourly_pollution.png`
* `weekday_pollution.png`
* `aqi_heatmap.png`

---

## How to Run

Install dependencies:

```bash
pip install pandas numpy matplotlib
```

Run the program:

```bash
python main.py
```

---

## Sample Insights

Possible findings may include:

* Winter months showing higher pollution levels.
* Rush hours experiencing increased AQI due to traffic.
* Weekdays having worse air quality than weekends.

These observations can help local authorities and residents better understand pollution patterns.

---

## Future Improvements

* Add multiple pollutant analysis (PM2.5, PM10, NO2, SO2).
* Use Seaborn for advanced visualizations.
* Build an AQI prediction model using Machine Learning.
* Create an interactive dashboard using Streamlit.

---

## Author

Sahaj
B.Tech Computer Science Engineering
