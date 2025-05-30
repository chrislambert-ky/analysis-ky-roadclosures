import os
import pandas as pd
from urllib.request import urlretrieve

def ensure_dirs():
    for d in [
        'data-raw', 'data-clean', 'data-reportready', 'temp']:
        os.makedirs(d, exist_ok=True)

def download_data():
    base_url = 'https://storage.googleapis.com/kytc-its-2020-openrecords/toc/KYTC-TOC-Weather-Closures-Historic-{}.csv'
    years = [2021, 2022, 2023, 2024, 2025]
    for year in years:
        url = base_url.format(year)
        out = f'data-raw/KYTC-TOC-Weather-Closures-Historic-{year}.csv'
        urlretrieve(url, out)

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

def process_and_clean():
    # Download and load data
    download_data()
    years = [2021, 2022, 2023, 2024, 2025]
    dfs = {}
    for year in years:
        df = pd.read_csv(f'data-raw/KYTC-TOC-Weather-Closures-Historic-{year}.csv')
        if year == 2021:
            clean_esri_link(df)
        else:
            clean_google_link(df)
        clean_tl(df)
        dfs[year] = df
        df.to_csv(f'data-clean/kytc-closures-{year}-clean.csv', index=False)
    # Standardize columns and remove negative durations
    col_order = ['District','County','Route','Road_Name','Begin_MP','End_MP','Comments','Reported_On','End_Date','latitude','longitude','Duration_Default','Duration_Hours']
    for year in years:
        dfs[year] = dfs[year][col_order]
        dfs[year] = dfs[year][dfs[year]['Duration_Hours'] > 0]
    # Merge all years
    df_all = pd.concat([dfs[y] for y in years])
    # Export reporting datasets
    df_all.to_csv('data-reportready/kytc-closures-2021-2025-report_dataset.csv', index=False)
    df_all.to_excel('data-reportready/kytc-closures-2021-2025-report_dataset.xlsx', index=False)
    df_all.to_parquet('data-reportready/kytc-closures-2021-2025-report_dataset.parquet', index=False)

def main():
    ensure_dirs()
    process_and_clean()

if __name__ == '__main__':
    main()



