import requests

api_key = "b6ccd944b89d6f56ce81e2f1eb24220f"
city_name = "karimnagar"
api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

response = requests.get(api_url)
data = response.json()

# Extract relevant weather data from the response
temperature = data['main']['temp']
humidity = data['main']['humidity']
wind_speed = data['wind']['speed']

print(f"Temperature: {temperature} K")
print(f"Humidity: {humidity} %")
print(f"Wind speed: {wind_speed} m/s")
