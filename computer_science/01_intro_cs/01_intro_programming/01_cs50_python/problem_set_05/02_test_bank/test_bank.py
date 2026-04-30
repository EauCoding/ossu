from bank import value

def main():
    pass

def test_value_hello():
    assert value("Hello") == 0

def test_value_h():
    assert value("How you doing?") == 20

def test_value_other():
    assert value("What's up?") == 100

if __name__ == "__main__":
    main()
