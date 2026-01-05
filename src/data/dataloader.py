import pandas as pd
from pathlib import Path

DATA_DIR = Path("data/curated")

def load_precipitation(gauge_id):
    """
    Load daily precipitation time series for a gauge.
    """
    path = DATA_DIR / "forcings" / f"{gauge_id}.csv"
    df = pd.read_csv(path)

    if "prcp(mm/day)" not in df.columns:
        raise ValueError("Expected column 'prcp(mm/day)' not found")

    return df[["year", "month", "day", "prcp(mm/day)"]]
