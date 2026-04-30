from numb3rs import validate

def main():
    test_simple_validate()
    test_hard_validate()
    test_high_validate()
    test_wrong_validate()

def test_simple_validate():
    assert validate("1.2.3.4")

def test_hard_validate():
    assert validate("127.0.0.1")

def test_high_validate():
    assert not validate("256.22.22.3")

def test_wrong_validate():
    assert not validate("cat")

if __name__ == "__main__":
    main()
