# https://openweathermap.org  (create free account on this url.)
import requests

api_key = "66e74deecce2656ad00e28ca86b05f45"

city = input("Enter your city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url) 
data = response.json()



if str(data["cod"]) == "200":
    temp = data["main"]["temp"] 
    humidity = data["main"]["humidity"] 
    description = data["weather"][0]["description"] 
    wind = data["wind"]["speed"]


    
    print("\nWeather Report") 
    print("Tempreture:", temp, "°C") 
    print("Humidity:", humidity, "%") 
    print("Condition:, {description.title()}")  
    print(f"Wind Speed: {wind} m/s")
    print("🌤 Weather Report")

    
else: 
    print("Error:", data.get("message", "Something went wrong"))