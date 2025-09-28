def main():
    user_word = input("Input: ")
    result = shorten(user_word)
    print(f"Output: {result}")

def shorten(word):
    output_word = ""
    for s in word:
        for c in "aeiouAEIOU":
            if s == c:
                break
            elif c == "U":
                output_word += s
    return output_word

if __name__ == "__main__":
    main()
