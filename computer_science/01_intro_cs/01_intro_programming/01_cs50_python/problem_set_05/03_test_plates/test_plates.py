from plates import is_valid

def test_is_valid_short():
    assert is_valid("CS50")

def test_is_valid_long():
    assert is_valid("ECTO88")

def test_is_valid_no_digit():
    assert is_valid("NRVOUS")

def test_is_valid_zero():
    assert not is_valid("CS05")

def test_is_valid_short_false():
    assert not is_valid("50")

def test_is_valid_alpha():
    assert not is_valid("PI3.14")

def test_is_valid_false():
    assert not is_valid("CS50P2")
