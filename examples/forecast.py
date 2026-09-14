import os

from weatherkit import WeatherClient
from weatherkit.formatting import format_forecast

client = WeatherClient(api_key=os.environ["WEATHERKIT_API_KEY"])
print(format_forecast(client.forecast("Berlin", days=5)))
