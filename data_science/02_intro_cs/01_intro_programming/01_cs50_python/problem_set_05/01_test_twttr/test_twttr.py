from twttr import shorten

def main():
    test_shorten_word()
    test_shorten_punctuation()
    test_shorten_number()

def test_shorten_word():
    assert shorten("twitter") == "twttr"

def test_shorten_punctuation():
    assert shorten("What's your name?") == "Wht's yr nm?"

def test_shorten_number():
    assert shorten("CS50") == "CS50"

if __name__ == "__main__":
    main()
