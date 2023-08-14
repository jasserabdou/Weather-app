import requests
import streamlit as st
from PIL import Image


def get_weather_data(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data


def main():
    st.title("Weather App 🌦️")
    st.write("Welcome to the Weather App! Enter your API key and a city name to get weather information.")

    # Display weather image
    image = Image.open("weather.jpeg")
    st.image(image, use_column_width=True)

    # User input for API key and city name
    api_key = st.text_input("Enter your API key", type="password")
    city = st.text_input("Enter city name")

    if not api_key or not city:
        st.warning("Please provide your API key and city name.")
        st.stop()

    # Fetch weather data
    if st.button("Get Weather"):
        try:
            weather_data = get_weather_data(api_key, city)

            if weather_data['cod'] == 200:
                weather_info = weather_data['main']
                st.header(
                    f"Weather in {weather_data['name']}, {weather_data['sys']['country']}")
                st.subheader(f"Temperature: {weather_info['temp']} °C")
                st.subheader(
                    f"Wind Speed: {weather_data['wind']['speed']} m/s")
                st.subheader(f"Cloudiness: {weather_data['clouds']['all']} %")
                st.subheader(f"Humidity: {weather_info['humidity']} %")
                st.subheader(f"Pressure: {weather_info['pressure']} hPa")
                st.subheader(
                    f"Timezone: {round(weather_data['timezone']*0.000277778, 2)} hours")
                st.subheader(
                    f"Description: {weather_data['weather'][0]['description']}")
            else:
                st.error(
                    "City not found. Please check the spelling or try a different city or you didn't enter full api key.")
        except requests.exceptions.RequestException:
            st.error("Error fetching weather data. Please try again later.")
        except Exception:
            st.error("An error occurred. Please try again later.")


if __name__ == "__main__":
    main()
