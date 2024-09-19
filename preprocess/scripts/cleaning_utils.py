from numpy import percentile
from pandas import DataFrame

def drop_outliers(
    dataframe: DataFrame, columns: list[str], percent: int = 75
) -> DataFrame:
    """
    With Tukey's method to find outliers, we change quartile by input percentile & drop outliers
    """
    for column in columns:
        if dataframe[column].dtype not in ["int64", "float64"]:
            continue
        first_quartile = percentile(dataframe[column], 100 - percent)
        third_quartile = percentile(dataframe[column], percent)
        step = 1.5 * (third_quartile - first_quartile)

        dataframe.drop(
            dataframe.loc[
                ~(
                    (dataframe[column] >= first_quartile - step)
                    & (dataframe[column] <= third_quartile + step)
                ),
                column,
            ].index,
            inplace=True,
        )
    return dataframe


def unite_floors_together(floor: str) -> str:
    if floor in ('Entreplanta interior', 'Entreplanta exterior'):
        floor = 'Entreplanta'
    elif floor in ('Semi-sótano interior', 'Semi-sótano exterior'):
        floor = 'Semi-sótano'
    elif floor in ('Sótano interior', 'Sótano exterior'):
        floor = 'Sótano'
    return floor