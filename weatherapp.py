import requests

API_KEY = "faebeb61a4c528757d056db30760861c"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {"q": city, "appid": API_KEY}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def main():
    while True:
        city = input("Enter a city name (or 'q' to quit): ")
        if city.lower() == "q":
            break

        weather_data = get_weather(city)

        if weather_data:
            temp = weather_data["main"]["temp"]
            description = weather_data["weather"][0]["description"]

            print(f"Current weather in {city}:")
            print(f"\tTemperature: {temp:.2f}°C")
            print(f"\tDescription: {description}")
        else:
            print("Error: Could not retrieve weather data.")

if __name__ == "__main__":
    main()
