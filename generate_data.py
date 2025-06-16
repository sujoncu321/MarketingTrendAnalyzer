import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

def generate_fake_data():
    today = datetime.today()
    dates = [today - timedelta(days=i) for i in range(30)]
    dates.reverse()

    data = {
        "date": [d.date() for d in dates],
        "visitors": np.random.randint(100, 1000, 30),
        "clicks": np.random.randint(20, 300, 30),
        "sales": np.random.randint(5, 100, 30)
    }

    df = pd.DataFrame(data)
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/marketing_data.csv", index=False)
    return df
