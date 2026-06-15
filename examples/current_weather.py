import os

from weatherkit import WeatherClient
from weatherkit.formatting import format_current

client = WeatherClient(api_key=os.environ["WEATHERKIT_API_KEY"])
print(format_current(client.current("Lisbon")))
