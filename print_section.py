import pathlib
from itertools import islice
path = pathlib.Path('etl_pipeline_final.py')
for idx, line in enumerate(path.open(), 1):
    if 30 <= idx <= 110:
        print(f"{idx}: {line.rstrip()}" )
