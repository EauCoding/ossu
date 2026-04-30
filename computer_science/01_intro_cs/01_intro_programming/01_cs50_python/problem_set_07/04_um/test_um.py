from um import count
import pytest

def test_word():
    assert count("hello, um, worl!") == 1

def test_not_word():
    assert count("yummy!") == 0

def test_punctuation():
    assert count("Um, thanks, um...") == 2
