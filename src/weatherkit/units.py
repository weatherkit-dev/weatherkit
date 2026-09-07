def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


def kmh_to_mph(kmh: float) -> float:
    return kmh / 1.609344


def hpa_to_inhg(hpa: float) -> float:
    return hpa * 0.0295299830714


def celsius_to_kelvin(celsius: float) -> float:
    return celsius + 273.15
