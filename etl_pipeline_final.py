import os
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

def ensure_dirs():
    for d in ['data-raw', 'data-clean', 'data-reportready', 'temp']:
        os.makedirs(d, exist_ok=True)
        logging.info(f"Ensured folder exists: {d}")

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
        df.drop_duplicates(inplace=True)
        df.to_csv(f"data-raw/KYTC-TOC-Weather-Closures-Historic-{year}.csv", index=False)
        dfs[year] = df
    return dfs

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

def process_and_save_cleaned(dfs):
    order = ['District','County','Route','Road_Name','Begin_MP','End_MP','Comments','Reported_On','End_Date','latitude','longitude','Duration_Default','Duration_Hours']
    cleaned = {}
    # 2021: ESRI link
    df2021 = clean_esri_link(dfs['2021'])
    df2021 = clean_tl(df2021)
    df2021 = df2021[order]
    # Filter out records where Reported_On is prior to 2021-01-01
    df2021 = df2021[df2021['Reported_On'] >= pd.Timestamp('2021-01-01')]
    df2021 = df2021[df2021['Duration_Hours'] > 0]
    df2021.to_csv("data-clean/kytc-closures-2021-clean.csv", index=False)
    cleaned['2021'] = df2021
    # 2022-2025: Google link
    for year in ['2022', '2023', '2024', '2025']:
        df = clean_google_link(dfs[year])
        df = clean_tl(df)
        df = df[order]
        df = df[df['Duration_Hours'] > 0]
        df.to_csv(f"data-clean/kytc-closures-{year}-clean.csv", index=False)
        cleaned[year] = df
    return cleaned

def merge_and_export(cleaned):
    col_order = ['District','County','Route','Road_Name','Begin_MP','End_MP','Comments','Reported_On','End_Date','latitude','longitude','Duration_Default','Duration_Hours']
    dfs = [cleaned[year] for year in ['2021','2022','2023','2024','2025']]
    df = pd.concat(dfs)
    df = df[col_order]
    # Remove duplicates based on latitude, longitude, Reported_On, and Comments
    df = df.drop_duplicates(subset=['latitude', 'longitude', 'Reported_On', 'Comments'])
    # CSV export with error handling
    try:
        df.to_csv("data-reportready/kytc-closures-2021-2025-report_dataset.csv", index=False)
        df.to_csv("data-reportready/kytc-closures-report_dataset.csv", index=False)
        logging.info("Exported merged dataset to CSV.")
    except Exception as e:
        logging.warning(f"CSV export failed: {e}")
    # XLSX export
    try:
        df.to_excel("data-reportready/kytc-closures-2021-2025-report_dataset.xlsx", index=False)
        df.to_excel("data-reportready/kytc-closures-report_dataset.xlsx", index=False)
        logging.info("Exported merged dataset to XLSX.")
    except Exception as e:
        logging.warning(f"Excel export failed: {e}")
    # Parquet export
    try:
        df.to_parquet("data-reportready/kytc-closures-2021-2025-report_dataset.parquet", index=False)
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
