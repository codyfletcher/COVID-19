import pandas as pd
from haversine import haversine, Unit
from pandas import DataFrame
from pandas.core.series import Series


def csv_to_dataframe(path: str) -> DataFrame:
    return pd.read_csv(path)


def df_haversine(lat1: float, lng1: float, lat2: float, lng2: float):
    # print(f"lat1: {lat1} is of type {type(lat1)}")
    # print(f"lat2: {lat2} is of type {type(lat2)}")
    return haversine((lat1, lng1), (lat2, lng2), Unit.MILES)
