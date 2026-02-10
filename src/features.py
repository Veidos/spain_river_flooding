import pandas as pd

def add_basic_datetime_features(df: pd.DataFrame, col: str) -> pd.DataFrame:
    df = df.copy()
    dt = pd.to_datetime(df[col])
    df["year"] = dt.dt.year
    df["month"] = dt.dt.month
    df["day"] = dt.dt.day
    return df
