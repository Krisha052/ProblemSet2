
def main():
    phrase = input("Input: ")
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"} #sets are more effective than lists for membership checking, better time complexity (immutable)
    updated_phrase = ""
    for char in phrase: #optimized version: updated_phrase = ''.join([char for char in phrase if char not in vowels])
        if char not in vowels:
            updated_phrase += char
    print(f"Output: {updated_phrase}")

if __name__ == "__main__":
    main()