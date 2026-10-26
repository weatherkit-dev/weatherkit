# Air quality

    from weatherkit.air_quality import band

    quality = client.air_quality("Milan")
    print(band(quality.pm10))

Bands follow the European air quality index for PM10: good (up to 20), fair (up to 40), moderate (up to 50), poor (up to 100), very poor (up to 150) and extremely poor (above 150). Values are in micrograms per cubic metre.
