# weatherkit
Python class for making WeatherKit requests

[WeatherKit REST API Documentation](https://developer.apple.com/documentation/weatherkitrestapi)

## Example
```
from weatherkit import WeatherKit

latitude = 37.332279
longitude = -122.010979
countryCode = "US"
dataSets = ['currentWeather', 'forecastDaily']
tz = "America/Cupertino"

query_parameters = [
	f'countryCode={countryCode}',
	f'dataSets={",".join(dataSets)}',
	f'timezone={tz}'
]

weather = WeatherKit().get_weather(latitude, longitude, query_parameters)
```