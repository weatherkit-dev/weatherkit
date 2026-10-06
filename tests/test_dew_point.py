from weatherkit.units import dew_point


def test_dew_point_at_full_humidity():
    assert round(dew_point(20, 100), 1) == 20.0


def test_dew_point_dry_air():
    assert dew_point(20, 30) < 5
