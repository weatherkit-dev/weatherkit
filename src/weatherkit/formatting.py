def format_current(data: dict, units: str = "metric") -> str:
    temp = data["temp_c"] if units == "metric" else data["temp_f"]
    symbol = "C" if units == "metric" else "F"
    return f"{data['city']}: {temp:.1f} {symbol}, {data['condition']}"


def format_forecast(days: list[dict], units: str = "metric") -> str:
    symbol = "C" if units == "metric" else "F"
    key = "max_c" if units == "metric" else "max_f"
    return "\n".join(f"{d['date']}: max {d[key]:.0f} {symbol}" for d in days)


def format_hourly(hours: list[dict], units: str = "metric") -> str:
    symbol = "C" if units == "metric" else "F"
    key = "temp_c" if units == "metric" else "temp_f"
    return "\n".join(f"{h['time']}: {h[key]:.0f} {symbol}" for h in hours)
