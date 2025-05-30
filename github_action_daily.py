# This script is being developed as part of the Code Kentucky Python Data Analyst pathway.
# 
# ---
# 
# Goal: Quantify the impact of road closures based on three metrics:
# 1) Total number of closures<br>
# 2) Frequency of closures<br>
# 3) Duration of closures.<br>
# 
# These are a few of the sample questions that I hope to answer:<br>
# 1) How many closures occur statewide each year? (Typical bar graph showing count per year?)<br>
# 2) How many road closures occur in each county per year? (Normal bar graph with year as x-axis and count of closures?)<br>
# 3) How often, or how frequently, is a single road being closed due to rainfall? (Horizonatal bar graph with roadname as Y axis or pivot table output?)<br>
# 4) What is the average duration of road closures?
# 
# DISCLAIMER:  Results may vary.  In addition to historic data, this notebook is also utilizing current year data.  The data source is updated every 1 hour but only when there are active road closures due to weather related events.
# 
# -Chris Lambert
# 
# ---

# | Field           | Data Type    | Description                                                                                               | Examples                   |
# |-----------------|--------------|-----------------------------------------------------------------------------------------------------------|----------------------------|
# | District        | Integer      | KYTC divides the state into 12 geographic regions. Districts start from 1 in the West to 12 in the East. | 1, 2, 3, etc.              |
# | County          | Object       | The name of the county where the event occurred. County names are proper case.                            | Fayette, Frankfort, etc.  |
# | Route           | Object       | The route name associated with the incident.                                                             | KY-80, US-60, I-69        |
# | Road_Name       | Object       | The name of the road associated with the transportation records.                                          | DONALDSON CREEK RD, etc. |
# | Begin_MP        | Float        | The milepost where the event or condition begins on the road.                                              | 10.5, 20.3, etc.           |
# | End_MP          | Float        | The milepost where the event or condition ends on the road.                                                | 15.2, 25.7, etc.           |
# | Comments        | Object       | Additional comments or information related to the transportation event.                                   | N/A                        |
# | Reported_On     | Datetime     | The date and time when the transportation event was reported. All reports are in Eastern Standard Time.   | YYYY-MM-DD HH:MM:SS       |
# | End_Date        | Datetime     | The date and time when the transportation event concluded or was resolved. All reports are in EST.        | YYYY-MM-DD HH:MM:SS       |
# | latitude        | Float        | The latitude coordinate associated with the location of the transportation event.                         | 38.1234, 39.5678, etc.    |
# | longitude       | Float        | The longitude coordinate associated with the location of the transportation event.                        | -84.5678, -85.1234, etc.  |
# | Duration_Default| Timedelta    | The default duration of the transportation event.                                                        | 0 days 01:30:00, etc.     |
# | Duration_Hours  | Float        | The duration of the transportation event in hours.                                                        | 1.5, 2.75, etc.            |
# 

# %%
#Pandas is used for data manipulation and analysis.
#Matplotlib is used for data visualization.
#os is used to create folders
#urlretrieve is used to download files from the internet

import pandas as pd
import matplotlib.pyplot as plt  # Not used in ETL, can be removed if not needed
import os
from urllib.request import urlretrieve
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

def create_folders():
    for folder in ['data-raw', 'data-clean', 'data-reportready', 'temp']:
        os.makedirs(folder, exist_ok=True)
        logging.info(f"Ensured folder exists: {folder}")

def download_data():
    urls = {
        '2021': 'https://storage.googleapis.com/kytc-its-2020-openrecords/toc/KYTC-TOC-Weather-Closures-Historic-2021.csv',
        '2022': 'https://storage.googleapis.com/kytc-its-2020-openrecords/toc/KYTC-TOC-Weather-Closures-Historic-2022.csv',
        '2023': 'https://storage.googleapis.com/kytc-its-2020-openrecords/toc/KYTC-TOC-Weather-Closures-Historic-2023.csv',
        '2024': 'https://storage.googleapis.com/kytc-its-2020-openrecords/toc/KYTC-TOC-Weather-Closures-Historic-2024.csv',
        '2025': 'https://storage.googleapis.com/kytc-its-2020-openrecords/toc/KYTC-TOC-Weather-Closures-Historic-2025.csv',
    }
    dfs = {}
    for year, url in urls.items():
        logging.info(f"Downloading data for {year} from {url}")
        df = pd.read_csv(url)
        df.to_csv(f"data-raw/KYTC-TOC-Weather-Closures-Historic-{year}.csv", index=False)
        dfs[year] = df
    return dfs

def clean_tl(df):
    df['End_Date'] = df['End_Date'].str.replace('+00:00', '')
    df['Reported_On'] = pd.to_datetime(df['Reported_On'])
    df['End_Date'] = pd.to_datetime(df['End_Date'])
    df['Duration_Default'] = df['End_Date'] - df['Reported_On']
    df['Duration_Hours'] = (df['Duration_Default'].dt.total_seconds() / 3600).round(4)
    df['Comments'] = df['Comments'].replace(r'[\r\n]+', ' ', regex=True)
    return df

def clean_esri_link(df):
    df['Route_Link'] = df['Route_Link'].str.replace(
        'https://kytc.maps.arcgis.com/apps/webappviewer/index.html?id=327a38decc8c4e5cb882dc6cd0f9d45d&zoom=14&center=',
        '')
    df[['longitude', 'latitude']] = df['Route_Link'].str.split(",", expand=True)
    df.drop('Route_Link', axis=1, inplace=True)
    return df

def clean_google_link(df):
    df['Route_Link'] = df['Route_Link'].str.replace('https://goky.ky.gov/?lat=','')
    df['Route_Link'] = df['Route_Link'].str.replace('&lng=',',')
    df['Route_Link'] = df['Route_Link'].str.replace('&.*', '', regex=True)
    df[['latitude','longitude']] = df.Route_Link.str.split(",",expand=True)
    df.drop('Route_Link', axis=1, inplace=True)
    return df

def process_and_save_cleaned(dfs):
    order = ['District','County','Route','Road_Name','Begin_MP','End_MP','Comments','Reported_On','End_Date','latitude','longitude','Duration_Default','Duration_Hours']
    # 2021: ESRI link
    df2021 = clean_esri_link(dfs['2021'])
    df2021 = clean_tl(dfs['2021'])
    df2021 = df2021[order]
    df2021 = df2021[df2021['Duration_Hours'] > 0]
    df2021.to_csv("data-clean/kytc-closures-2021-clean.csv", index=False)
    # 2022-2025: Google link
    cleaned = {}
    for year in ['2022', '2023', '2024', '2025']:
        df = clean_google_link(dfs[year])
        df = clean_tl(dfs[year])
        df = df[order]
        df = df[df['Duration_Hours'] > 0]
        df.to_csv(f"data-clean/kytc-closures-{year}-clean.csv", index=False)
        cleaned[year] = df
    cleaned['2021'] = df2021
    return cleaned

def merge_and_export(cleaned):
    col_order = ['District','County','Route','Road_Name','Begin_MP','End_MP','Comments','Reported_On','End_Date','latitude','longitude','Duration_Default','Duration_Hours']
    dfs = [cleaned[year] for year in ['2021','2022','2023','2024','2025']]
    df = pd.concat(dfs)
    df = df[col_order]
    df.to_csv("data-reportready/kytc-closures-2021-2025-report_dataset.csv", index=False)
    try:
        df.to_excel("data-reportready/kytc-closures-2021-2025-report_dataset.xlsx", index=False)
    except Exception as e:
        logging.warning(f"Excel export failed: {e}")
    try:
        df.to_parquet("data-reportready/kytc-closures-2021-2025-report_dataset.parquet", index=False)
    except Exception as e:
        logging.warning(f"Parquet export failed: {e}")
    logging.info("Exported merged datasets to CSV, XLSX, and Parquet.")

def main():
    create_folders()
    dfs = download_data()
    cleaned = process_and_save_cleaned(dfs)
    merge_and_export(cleaned)

if __name__ == "__main__":
    main()

