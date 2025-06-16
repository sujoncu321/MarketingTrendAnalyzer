import pandas as pd

def process_data():
    df = pd.read_csv("data/marketing_data.csv", parse_dates=["date"])
    df = df.sort_values("date")
    df["conversion_rate"] = df["sales"] / df["visitors"]
    df.to_csv("data/processed_data.csv", index=False)
    return df
