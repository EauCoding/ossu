from io import StringIO
from contextlib import redirect_stdout

import pytest

from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12

def test_str():
    jar = Jar()
    jar.deposit(1)

    buffer = StringIO()
    with redirect_stdout(buffer):
        print(jar)
    output = buffer.getvalue().strip()

    assert output == '🍪'

def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.deposit(13)

def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.withdraw(5)
