import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def predict_sales(days=7):
    df = pd.read_csv("data/processed_data.csv", parse_dates=["date"])
    df["day_index"] = range(len(df))

    X = df[["day_index"]]
    y = df["sales"]

    model = LinearRegression()
    model.fit(X, y)

    future_indexes = np.array(range(len(df), len(df) + days)).reshape(-1, 1)
    predictions = model.predict(future_indexes)

    prediction_df = pd.DataFrame({
        "day_index": future_indexes.flatten(),
        "predicted_sales": predictions
    })
    return prediction_df
