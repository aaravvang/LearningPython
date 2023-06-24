import requests
import json

location = input("Enter the location you want, and I will give you the weather forecast:")


#string interpolation
urlTwo = f"http://api.weatherapi.com/v1/forecast.json?key=26fee625beaa49ed9bb192910232904&q={location}&days=3"

w = requests.get(urlTwo)
# print(w.text)

j=json.loads(w.text) #converts text data to dictionary


region = j["location"]["region"]
country = j["location"]["country"]
print("\nWEATHER APP BY AARAV\n")
print("Location : ",location)
print("Country : ",country)
print("Region : ",region)

for i in range(0,3):
  dayHighF = j["forecast"]["forecastday"][i]["day"]["maxtemp_f"]
  dayLowF = j["forecast"]["forecastday"][i]["day"]["mintemp_f"]
  avgTempF = j["forecast"]["forecastday"][i]["day"]["avgtemp_f"]
  maxWindMph = j["forecast"]["forecastday"][i]["day"]["maxwind_mph"]
  conditionOne = j["forecast"]["forecastday"][i]["day"]["condition"]["text"]

  print("\n DAY", i+1)
  print("High:",dayHighF)
  print("Low:", dayLowF)
  print("avg temp:",avgTempF)
  print("Max Wind speed:", maxWindMph)
  print("condition:", conditionOne)

  






