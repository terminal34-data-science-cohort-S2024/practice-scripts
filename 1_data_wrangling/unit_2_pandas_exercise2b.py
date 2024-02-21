"""
Exercise #2b: Basic Data Retrieval with API Requests

Scenario

You need to retrieve data about the current weather in San Juan, Puerto Rico, using the OpenWeatherMap API.

API Endpoint and Key

To access the OpenWeatherMap API, you will need an API key. You can sign up for a free API key at [OpenWeatherMap](https://openweathermap.org/api). The endpoint for current weather data is:

```
https://api.openweathermap.org/data/2.5/weather?q=San%20Juan,PR&appid=YOUR_API_KEY
```

Replace `YOUR_API_KEY` with your actual API key.

Tasks
Fetch Weather Data:
Use Python to make a request to the OpenWeatherMap API and retrieve weather data for San Juan, Puerto Rico.
Parse and Display Data:
Parse the JSON data returned from the API.
Extract and print the following information:
City name
Current temperature (in Celsius)
Weather description
Humidity
Handle API Errors:
Check for any API errors (like invalid API key or network issues) and print an appropriate message.

Implementation

You will need to implement a Python solution for this exercise. Ensure you have the `requests` and `pandas` libraries installed, and optionally `matplotlib` for plotting.
"""
