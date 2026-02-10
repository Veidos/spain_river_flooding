from pathlib import Path
import pandas as pd
from .config import DATA_RAW_DIR, DATA_PROCESSED_DIR

def load_raw_csv(filename: str) -> pd.DataFrame:
    path = DATA_RAW_DIR / filename
    return pd.read_csv(path)

def save_processed_df(df: pd.DataFrame, filename: str) -> Path:
    path = DATA_PROCESSED_DIR / filename
    df.to_csv(path, index=False)
    return path
