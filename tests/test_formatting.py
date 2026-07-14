from weatherkit.formatting import format_current, format_forecast


def test_metric():
    data = {"city": "Madrid", "temp_c": 20.04, "temp_f": 68.1, "condition": "Sunny"}
    assert format_current(data) == "Madrid: 20.0 C, Sunny"


def test_forecast_never_prints_minus_zero():
    days = [{"date": "2026-01-10", "max_c": -0.3, "max_f": 31.5}]
    assert format_forecast(days) == "2026-01-10: max 0 C"
