import os
import pickle
from typing import Dict, Any
import numpy as np
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from src.exception import CustomException


def save_object(file_path: str, obj: Any) -> None:
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e)


def load_object(file_path: str) -> Any:
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise CustomException(e)


def evaluate_models(
    X_train,
    y_train,
    X_test,
    y_test,
    models: Dict,
    params: Dict
) -> Dict:
    try:
        report = {}
        for model_name, model in models.items():
            param_grid = params.get(model_name, {})
            gs = GridSearchCV(model, param_grid, cv=3, n_jobs=-1)
            gs.fit(X_train, y_train)
            best_model = gs.best_estimator_
            y_train_pred = best_model.predict(X_train)
            y_test_pred = best_model.predict(X_test)
            train_score = r2_score(y_train, y_train_pred)
            test_score = r2_score(y_test, y_test_pred)
            report[model_name] = {
                "train_score": train_score,
                "test_score": test_score,
                "best_params": gs.best_params_
            }
        return report
    except Exception as e:
        raise CustomException(e)