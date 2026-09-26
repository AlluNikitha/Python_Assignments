# Week 4 – Capstone Project: COVID-19 Data Tracker

## Dataset

COVID-19 Dataset (Our World in Data). The script automatically
downloads the "latest snapshot" file (one row per country with the
most recent cumulative totals) from OWID's public GitHub repository
the first time it runs, and reuses the saved copy on later runs.

## Tasks

- Load data using Pandas
- Display top 5 countries by total cases
- Plot bar chart (Matplotlib)

**Skill Gain:** Data visualization + analysis.

## Requirements

```
pip install pandas matplotlib requests
```

## Run

```
python covid_tracker.py
```

Prints the top 5 countries by total confirmed cases, and saves/opens
a bar chart as `top5_covid_cases.png`.

## Note

The dataset includes aggregate rows (continents, income groups,
"World") mixed in alongside real countries. These are filtered out
using the `continent` column, which is empty only for aggregate rows.
