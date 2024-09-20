from typing import Literal, TypeAlias
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline 
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR

Models: TypeAlias = LinearRegression | SVR | DecisionTreeRegressor

class CustomEncoder(BaseEstimator, TransformerMixin):
    pass    

def pipeline_model(model: Models) -> Pipeline:
    if not isinstance(LinearRegression, model) and not isinstance(SVR, model) and not isinstance(DecisionTreeRegressor, model):
        raise NotImplementedError 
    return Pipeline([('encoding', CustomEncoder()),('standardisation', StandardScaler()),('model', model())])