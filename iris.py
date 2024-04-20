from typing import Any, List, Type

from joblib import load
from pydantic import BaseModel

class IrisSingleRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class IrisBatchRequest(BaseModel):
    features: List[IrisSingleRequest]



class IrisPredictor:
    def __init__(self):
        self.model = load('model.sav')
        self.mapping_res = {0: "setosa", 1: "versicolor", 2: "virginica"}

    def post_process(self, pred: Any):
        return self.mapping_res[pred]

    def predict(self, features: List[IrisSingleRequest]) -> Type[Any]:
        formatted_features = [
            [
                item.sepal_length,
                item.sepal_width,
                item.petal_length,
                item.petal_width,
            ]
            for item in features
        ]

        prediction_result = self.model.predict(formatted_features)

        res = []
        for feature, pred in zip(features, list(prediction_result)):
            post_process_pred = self.post_process(pred)
            res.append(post_process_pred)


        return {'result': res}
