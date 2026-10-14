from weatherkit.air_quality import band, parse_air_quality


def test_bands():
    assert band(15) == "good"
    assert band(120) == "very poor"
    assert band(300) == "extremely poor"


def test_parse():
    quality = parse_air_quality({"city": "Milan", "pm2_5": 18.2, "pm10": 31.0})
    assert band(quality.pm10) == "fair"
