import os
from datetime import datetime
from pathlib import Path

import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

def ensure_dirs():
    for d in ['data-raw', 'data-clean', 'data-reportready', 'temp']:
        os.makedirs(d, exist_ok=True)
        logging.info(f"Ensured folder exists: {d}")

def download_data(year=None):
    year = year or datetime.now().year
    url = (
        f"https://storage.googleapis.com/kytc-its-2020-openrecords/toc/"
        f"KYTC-TOC-Weather-Closures-Historic-{year}.csv"
    )
    logging.info(f"Downloading data for {year} from {url}")
    df = pd.read_csv(url)
    df.drop_duplicates(inplace=True)
    raw_path = f"data-raw/KYTC-TOC-Weather-Closures-Historic-{year}.csv"
    df.to_csv(raw_path, index=False)
    return {str(year): df}

def clean_tl(df):
    df['End_Date'] = df['End_Date'].str.replace('+00:00', '', regex=False)
    df['Reported_On'] = pd.to_datetime(df['Reported_On'])
    df['End_Date'] = pd.to_datetime(df['End_Date'])
    df['Duration_Default'] = df['End_Date'] - df['Reported_On']
    df['Duration_Hours'] = (df['Duration_Default'].dt.total_seconds() / 3600).round(4)
    df['Comments'] = df['Comments'].replace(r'[\r\n]+', ' ', regex=True)
    return df

def clean_esri_link(df):
    df['Route_Link'] = df['Route_Link'].str.replace(
        'https://kytc.maps.arcgis.com/apps/webappviewer/index.html?id=327a38decc8c4e5cb882dc6cd0f9d45d&zoom=14&center=', '', regex=False)
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

def drop_duplicate_events(df):
    subset = ['District','County','Route','Road_Name','Begin_MP','End_MP',
              'Comments','Reported_On','End_Date','latitude','longitude',
              'Duration_Default','Duration_Hours']
    return df.sort_values(by='End_Date', ascending=False).drop_duplicates(subset=subset)

def process_and_save_cleaned(dfs):
    order = ['District','County','Route','Road_Name','Begin_MP','End_MP','Comments','Reported_On','End_Date','latitude','longitude','Duration_Default','Duration_Hours']
    cleaned = {}
    clean_dir = Path('data-clean')
    for stale in clean_dir.glob('kytc-closures-*-clean.csv'):
        stale.unlink()
    for year in sorted(dfs.keys(), key=int):
        df = dfs[year].copy()
        if 'Route_Link' in df.columns:
            detector = df['Route_Link'].dropna()
            if detector.empty:
                raise ValueError('Route_Link column is empty; cannot parse coordinates')
            sample = detector.iloc[0].lower()
            if 'goky.ky.gov' in sample:
                df = clean_google_link(df)
            elif 'maps.arcgis.com' in sample:
                df = clean_esri_link(df)
            else:
                raise ValueError(f"Cannot determine how to clean Route_Link values: {sample}")
        df = clean_tl(df)
        df = df[order]
        df = df[df['Duration_Hours'] > 0]
        df = df[df['Reported_On'] >= pd.Timestamp('2021-01-01')]
        df = drop_duplicate_events(df)
        df['Reported_Year'] = df['Reported_On'].dt.year
        for reported_year, partition in df.groupby('Reported_Year'):
            partition = partition.drop(columns='Reported_Year').copy()
            year_key = str(reported_year)
            if year_key in cleaned:
                combined = pd.concat([cleaned[year_key], partition], ignore_index=True)
                combined = drop_duplicate_events(combined)
                cleaned[year_key] = combined
            else:
                cleaned[year_key] = partition
            clean_path = f"data-clean/kytc-closures-{year_key}-clean.csv"
            cleaned[year_key].to_csv(clean_path, index=False)
    return cleaned

def merge_and_export(cleaned):
    col_order = ['District','County','Route','Road_Name','Begin_MP','End_MP','Comments','Reported_On','End_Date','latitude','longitude','Duration_Default','Duration_Hours']
    dfs = [cleaned[year] for year in sorted(cleaned.keys(), key=int)]
    df = pd.concat(dfs)
    df = df[col_order]
    # Keep most recent record for each location/comment tuple before dedup
    df = df.sort_values(by='End_Date', ascending=False)
    df = df.drop_duplicates(subset=['District','County','Route','Road_Name','Begin_MP','End_MP',
                                   'Comments','Reported_On','End_Date','latitude','longitude',
                                   'Duration_Default','Duration_Hours'])
    # CSV export with error handling
    try:
        df.to_csv("data-reportready/kytc-closures-report_dataset.csv", index=False)
        logging.info("Exported merged dataset to CSV.")
    except Exception as e:
        logging.warning(f"CSV export failed: {e}")
    # XLSX export
    try:
        df.to_excel("data-reportready/kytc-closures-report_dataset.xlsx", index=False)
        logging.info("Exported merged dataset to XLSX.")
    except Exception as e:
        logging.warning(f"Excel export failed: {e}")
    # Parquet export
    try:
        df.to_parquet("data-reportready/kytc-closures-report_dataset.parquet", index=False)
        logging.info("Exported merged dataset to Parquet.")
    except Exception as e:
        logging.warning(f"Parquet export failed: {e}")
    logging.info("Exported merged datasets to CSV, XLSX, and Parquet.")

def main():
    ensure_dirs()
    dfs = download_data()
    cleaned = process_and_save_cleaned(dfs)
    merge_and_export(cleaned)

if __name__ == "__main__":
    main()
