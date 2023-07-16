import requests
import streamlit as st
from PIL import Image


def get_weather_data(city):
    # get your api key in this link https://home.openweathermap.org/api_keys
    api_key = "YOUR_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data


def main():
    image = Image.open("weather.jpeg")
    st.image(image, use_column_width=True)
    st.title("Weather App 🌦️")
    city = st.text_input("Enter city name:")
    if st.button("Get Weather"):
        st.write("#### Fetching weather data...")
        try:
            weather_data = get_weather_data(city)

            if weather_data['cod'] == 200:
                st.header(
                    f"Location: {weather_data['name']}, {weather_data['sys']['country']}")
                st.subheader(f"Temperature: {weather_data['main']['temp']} °C")
                st.subheader(
                    f"Wind speed: {weather_data['wind']['speed']} meter/sec")
                st.subheader(f"Clouds: {weather_data['clouds']['all']} %")
                st.subheader(f"Humidity: {weather_data['main']['humidity']} %")
                st.subheader(
                    f"Pressure: {weather_data['main']['pressure']} hPa")
                st.subheader(
                    f"Timezone: {round(weather_data['timezone']*0.000277778,2)} hours")
                st.subheader(
                    f"Description: {weather_data['weather'][0]['description']}")
            else:
                st.error(
                    "City not found. Please check the spelling or try a different city.")
        except requests.exceptions.RequestException as e:
            st.error("Error fetching weather data. Please try again later.")
        except Exception as e:
            st.error("An error occurred. Please try again later.")


if __name__ == "__main__":
    main()
