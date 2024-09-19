from collections import Counter
from pandas import DataFrame

def counter_columns(dataframe: DataFrame, columns: list[str]) -> None:
    for column in columns:
        print(f"The counter of {column} is : {Counter(dataframe[column])}")
