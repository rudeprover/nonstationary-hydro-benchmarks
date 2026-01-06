from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data" / "curated"

def load_precipitation(gauge_id):
    path = DATA_DIR / "forcings" / f"{gauge_id}.csv"
    df = pd.read_csv(path)

    if "prcp(mm/day)" not in df.columns:
        raise ValueError("Expected column 'prcp(mm/day)' not found")

    return df[["year", "month", "day", "prcp(mm/day)"]]
