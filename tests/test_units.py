from weatherkit.units import celsius_to_fahrenheit, celsius_to_kelvin, fahrenheit_to_celsius, kmh_to_mph


def test_round_trip():
    assert round(fahrenheit_to_celsius(celsius_to_fahrenheit(21.5)), 6) == 21.5


def test_freezing_point():
    assert celsius_to_fahrenheit(0) == 32


def test_wind_speed():
    assert round(kmh_to_mph(100), 2) == 62.14


def test_kelvin():
    assert celsius_to_kelvin(0) == 273.15
