from fuel import convert, gauge
import pytest

def test_convert_quarter():
    assert convert("3/4") == 75

def test_convert_third():
    assert convert("1/3") == 33

def test_convert_zero_div():
    with pytest.raises(ZeroDivisionError):
        convert("100/0")

def test_convert_not_int():
    with pytest.raises(ValueError):
        convert("three/four")

def test_convert_large():
    with pytest.raises(ValueError):
        convert("10/3")

def test_convert_neg():
    with pytest.raises(ValueError):
        convert("-1/3")

def test_gauge_zero():
    assert gauge(0) == "E"

def test_gauge_one():
    assert gauge(1) == "E"

def test_gauge_full():
    assert gauge(100) == "F"

def test_gauge_almost_full():
    assert gauge(99) == "F"

def test_gauge_other():
    assert gauge(33) == "33%"
