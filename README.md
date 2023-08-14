# Weather App 🌦️

This is a simple Weather App built with Python, Streamlit, and the OpenWeatherMap API. It allows you to retrieve weather information for a specific city.

## Setup

1. Clone the repository to your local machine:

```bash
git clone https://github.com/jasserabdou/Weather-app.git
```

2. Install the required packages using pip:

```bash
pip install -r requirments.txt
```

3. Obtain an API key from [OpenWeatherMap](https://home.openweathermap.org/api_keys) by signing up for an account.

4. Replace `"YOUR_API_KEY"` in the code with the API key you obtained from OpenWeatherMap:

```python
api_key = "YOUR_API_KEY" 
```

## Usage

1. Run the Streamlit app using the following command:

```bash
streamlit run app.py
```

2. The app will open in your default web browser.

3. Enter the name of the city you want to get weather information for in the provided input field.

4. Click the "Get Weather" button to retrieve and display weather data for the specified city.

## Features

- Displays weather information such as temperature, wind speed, clouds, humidity, pressure, timezone, and weather description for the selected city.
- The app uses the OpenWeatherMap API to fetch weather data in real-time.
- deployed to this link https://weatherappbyjasser.streamlit.app/

## Requirements

- Python 3.9 or higher
- Streamlit
- Requests
- Pillow (PIL)




