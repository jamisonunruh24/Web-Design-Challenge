import pandas as pd

weather_data = "C:\Assignments\Web-Design-Challenge\WebVisualizations\Resources\Weather_data.csv"

weather_df = pd.read_csv(weather_data)
weather_df = weather_df.drop(['Unnamed: 0'], axis=1)
print(weather_df.head(2))