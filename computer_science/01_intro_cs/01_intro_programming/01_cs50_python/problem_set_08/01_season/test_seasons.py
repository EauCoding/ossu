from datetime import date, datetime, time

from seasons import check_dob_format, get_time_difference, get_time_str_formatted


def test_format():
    assert check_dob_format("2024-08-30") == datetime.strptime("2024-08-30", "%Y-%m-%d")

def test_difference():
    assert get_time_difference(datetime.strptime("2024-08-30", "%Y-%m-%d")) == 525600

def test_formatted():
    assert get_time_str_formatted(525600) == "Five hundred twenty-five thousand, six hundred minutes"