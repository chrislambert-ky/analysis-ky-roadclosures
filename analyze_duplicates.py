import pandas as pd
from collections import Counter
import os

def analyze_duplicates(csv_path, timestamp_cols=None, group_cols=None, output_summary=True):
    print(f"Analyzing: {csv_path}")
    df = pd.read_csv(csv_path)
    print(f"Total rows: {len(df)}")

    # Duplicates based on latitude, longitude, reported_on, and comments
    match_cols = ['Route', 'Road_Name', 'Begin_MP', 'Comments', 'Reported_On', 'Route_Link']
    for col in match_cols:
        if col not in df.columns:
            raise ValueError(f"Column '{col}' not found in CSV file.")
    dupes = df[df.duplicated(subset=match_cols, keep=False)]
    print(f"Duplicates (identical on {match_cols}): {len(dupes)}")

    # Summary by group_cols (e.g., road/location)
    if group_cols:
        summary = df.groupby(group_cols).size().reset_index(name='count')
        summary = summary.sort_values('count', ascending=False)
        print(f"\nMost frequent duplicates by {group_cols}:")
        print(summary.head(10))
    else:
        summary = None

    # Optionally output summary tables
    if output_summary:
        base = os.path.splitext(os.path.basename(csv_path))[0]
    dupes.to_csv(f"{base}_duplicates.csv", index=False)
    if summary is not None:
        summary.to_csv(f"{base}_duplicate_summary.csv", index=False)
    print("Summary files saved.")

if __name__ == "__main__":
    # Example usage: analyze 2021 file
    csv_file = "data-raw/KYTC-TOC-Weather-Closures-Historic-2021.csv"
    # Adjust these columns as needed for your schema
    timestamp_columns = ['Reported_On', 'End_Date']
    group_columns = ['District', 'County', 'Route', 'Road_Name']
    analyze_duplicates(csv_file, timestamp_cols=timestamp_columns, group_cols=group_columns)
    # To analyze other years, change csv_file path
