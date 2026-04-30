from working import convert
import pytest

def main():
    pass

def test_full_format():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_short_format():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_half_format():
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"

def test_wrong_minute():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

def test_wrong_hour():
    with pytest.raises(ValueError):
        convert("9:00 AM to 17:00 PM")

def test_wrong_format():
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")

if __name__ == "__main__":
    main()
