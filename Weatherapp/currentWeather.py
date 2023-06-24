import requests
import json

location = input("Enter the location you want, and I will give you the weather:")

url = f"http://api.weatherapi.com/v1/current.json?key=26fee625beaa49ed9bb192910232904&q={location}" #string interpolation

w = requests.get(url)
# print(w.text)

j=json.loads(w.text) #converts text data to dictionary

celcius=j["current"]["temp_c"]
fahrenheit = j["current"]["temp_f"]
region = j["location"]["region"]
country = j["location"]["country"]
condition = j["current"]["condition"]["text"]
windmph = j["current"]["wind_mph"]
winddir = j["current"]["wind_dir"]
humidity = j["current"]["humidity"]
pressure = j["current"]["pressure_mb"]



print("\nWEATHER APP BY AARAV\n")
print("Location : ",location)
print("Country : ",country)
print("Region : ",region)
print("Temperature in Celcius : ",celcius)
print("Temperature in Farenheit : ",fahrenheit)
print("Conditon : ", condition)
print("Wind in mph : ", windmph)
print("Wind direction :", winddir)
print("Humiditiy : ", humidity, "%")
print("Pressure : ", pressure)

# print(f"The current tempertaure in {location} is {celcius} degree celcius and {fahrenheit} degrees fahrenheit. Your location is in the {region} region and in the country of {country}. The current condition in your location is {condition}")





