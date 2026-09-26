"""
Capstone Project (Week 4): COVID-19 Data Tracker
Dataset: COVID-19 Dataset (Our World in Data)

Tasks:
- Load data using Pandas
- Display top 5 countries by total cases
- Plot bar chart (Matplotlib)

Skill Gain: Data visualization + analysis.

Setup:
    pip install pandas matplotlib requests
"""

import os
import requests
import pandas as pd
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(SCRIPT_DIR, "owid-covid-latest.csv")

# "Latest snapshot" dataset - one row per country with the most
# recent cumulative totals (much smaller and faster than the full
# multi-year daily time series).
DATA_URL = (
    "https://raw.githubusercontent.com/owid/covid-19-data/"
    "master/public/data/latest/owid-covid-latest.csv"
)


def download_data_if_needed():
    if os.path.exists(DATA_FILE):
        print("Using cached dataset file.")
        return
    print("Downloading COVID-19 dataset...")
    response = requests.get(DATA_URL, timeout=30)
    response.raise_for_status()
    with open(DATA_FILE, "wb") as f:
        f.write(response.content)
    print("Download complete.")


def load_data():
    df = pd.read_csv(DATA_FILE)
    print(f"Loaded data for {len(df)} locations.\n")
    return df


def get_top_countries(df, n=5):
    # The dataset includes non-country aggregate rows (continents,
    # income groups, "World", etc.) which all have an empty
    # "continent" column. Real countries always have one, so this
    # filters the aggregates out.
    countries_only = df[df["continent"].notna()]

    top = countries_only.nlargest(n, "total_cases")[["location", "total_cases"]]
    return top


def plot_bar_chart(top_countries):
    plt.figure(figsize=(8, 5))
    plt.bar(top_countries["location"], top_countries["total_cases"], color="steelblue")
    plt.title("Top 5 Countries by Total COVID-19 Cases")
    plt.xlabel("Country")
    plt.ylabel("Total Cases")
    plt.ticklabel_format(style="plain", axis="y")
    plt.tight_layout()

    output_path = os.path.join(SCRIPT_DIR, "top5_covid_cases.png")
    plt.savefig(output_path)
    print(f"\nChart saved to '{output_path}'.")
    plt.show()


def main():
    download_data_if_needed()
    df = load_data()

    top5 = get_top_countries(df, n=5)
    print("Top 5 countries by total cases:")
    print(top5.to_string(index=False))

    plot_bar_chart(top5)


if __name__ == "__main__":
    main()