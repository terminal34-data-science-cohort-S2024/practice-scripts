import pandas as pd
from random import randint, choice, uniform

# Generate a sample dataset
rr = 1000
data = {
    "datetime": pd.date_range(start="2023-01-01", periods=rr, freq='h'),
    "season": [choice([1, 2, 3, 4]) for _ in range(rr)],
    "holiday": [choice([0, 1]) for _ in range(rr)],
    "workingday": [choice([0, 1]) for _ in range(rr)],
    "weather": [choice([1, 2, 3, 4]) for _ in range(rr)],
    "temp": [round(uniform(5.0, 35.0), 2) for _ in range(rr)],
    "humidity": [randint(30, 90) for _ in range(rr)],
    "windspeed": [round(uniform(0, 50), 2) for _ in range(rr)],
    "casual": [randint(0, 300) for _ in range(rr)],
    "registered": [randint(0, 1000) for _ in range(rr)],
}

data["count"] = [x + y for x, y in zip(data["casual"], data["registered"])]

df = pd.DataFrame(data)
df.to_csv('unit_1_feature_engineering_exercise_data.csv')
