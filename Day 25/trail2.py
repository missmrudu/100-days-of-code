import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])
data_dict = data.to_dict()
print(data_dict)

print(data["temp"].mean())
print(data["temp"].max() )

print(data["condition"])
print(data.condition)

print(data[data.day == "Monday"])
