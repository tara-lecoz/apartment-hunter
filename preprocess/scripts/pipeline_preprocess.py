from pandas import DataFrame, concat
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer



def pipeline_model(dataframe) -> DataFrame:
    categorical_columns = [column for column in dataframe.columns if dataframe[column].dtype == 'object']
    numerical_columns = [column for column in dataframe.columns if dataframe[column].dtype in ['int64', 'float64']]

    encoder=OneHotEncoder(sparse=False)
    encoder.set_output(transform='pandas')
    dataframe[categorical_columns] = e
    scaler = StandardScaler()
    dataframe = scaler.fit_transform(dataframe)

    return dataframe