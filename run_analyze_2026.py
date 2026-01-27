from analyze_duplicates import analyze_duplicates

analyze_duplicates(
    'data-clean/kytc-closures-2026-clean.csv',
    exact_duplicates=True,
    group_cols=['District', 'County', 'Route', 'Road_Name']
)
