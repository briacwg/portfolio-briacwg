import pandas as pd


def load_csv(url: str) -> pd.DataFrame:
    return pd.read_csv(url)


def load_json(url: str) -> pd.DataFrame:
    return pd.read_json(url)


datasets = [
    {
        "url": "https://rhodyexchange.org/dataset/AAPL.csv",
        "short_name": "apple_stock",
        "load_function": load_csv,
    },
    {
        "url": "https://rhodyexchange.org/dataset/GOOG.json",
        "short_name": "google_stock",
        "load_function": load_json,
    },
    {
        "url": "https://rhodyexchange.org/dataset/TSLA.csv",
        "short_name": "tesla_stock",
        "load_function": load_csv,
    },
]
