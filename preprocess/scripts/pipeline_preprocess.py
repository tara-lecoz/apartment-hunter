from pandas import DataFrame, concat
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder




def pipeline_model(dataframe) -> DataFrame:
    categorical_columns = [column for column in dataframe.columns if dataframe[column].dtype == 'object']
    numerical_columns = [column for column in dataframe.columns if dataframe[column].dtype in ['int64', 'float64']]
    all_columns = dataframe.columns

    encoder=OneHotEncoder(sparse_output=False)
    encoder.set_output(transform='pandas')
    dataframe_categorical = encoder.fit_transform(dataframe[categorical_columns])

    dataframe.drop(columns=categorical_columns, inplace=True)
    dataframe = concat([dataframe, dataframe_categorical], axis=1)
    
    scaler = StandardScaler()
    for column in numerical_columns:
        dataframe[[column]] = scaler.fit_transform(dataframe[[column]])
    
    return dataframe