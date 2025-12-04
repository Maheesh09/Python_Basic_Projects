import requests
API_KEY = "455a708c11bd563bd4bcb98890e8debf"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city):

    params = {
    'q': city,
    'appid': API_KEY,
    'units': 'metric'
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)

    except requests.RequestException as e:
        print(f"Error connecting to the weather service: {e}")
        return None, None, None    

    if response.status_code != 200:
        print("Wrong city name or API error.")
        return None, None, None
    
    data = response.json()
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]
    

    return temp, humidity, description

def main():

    city = input("Enter city Name: ")

    if city is None or city.strip() == "":
        print("City name cannot be empty.")
        return
    
    temp, humidity,description = get_weather_data(city)
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {description}")

    


main()