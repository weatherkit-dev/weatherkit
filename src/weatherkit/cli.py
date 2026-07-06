import argparse
import os

from weatherkit.client import WeatherClient
from weatherkit.formatting import format_current, format_forecast


def main() -> None:
    parser = argparse.ArgumentParser(prog="weatherkit")
    sub = parser.add_subparsers(dest="command", required=True)
    current = sub.add_parser("current")
    current.add_argument("city")
    current.add_argument("--units", choices=["metric", "imperial"], default="metric")
    forecast = sub.add_parser("forecast")
    forecast.add_argument("city")
    forecast.add_argument("--days", type=int, default=3)
    forecast.add_argument("--units", choices=["metric", "imperial"], default="metric")
    alerts = sub.add_parser("alerts")
    alerts.add_argument("city")
    args = parser.parse_args()
    client = WeatherClient(api_key=os.environ["WEATHERKIT_API_KEY"])
    if args.command == "current":
        print(format_current(client.current(args.city), args.units))
    elif args.command == "forecast":
        print(format_forecast(client.forecast(args.city, args.days), args.units))
    else:
        for alert in client.alerts(args.city):
            print(f"{alert.severity.name}: {alert.title} ({alert.area})")
