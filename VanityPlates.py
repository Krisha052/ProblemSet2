
"""program planning:
- at least 2 letters
- between 2-6 characters
- numbers at the end (if any)
- first number cannot be 0
- only alphabets and numbers allowed 
"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    number_count = 0
    if not (2 <= len(s) <= 6):
        return False
    for char in s:
        if not (char.isnumeric() or char.isalpha()):
            return False
        elif char.isnumeric() and number_count == 0:
            if char == "0":
                return False
            elif not (s[s.index(char):].isnumeric()):
                return False
            else:
                number_count += 1
    return True

if __name__ == "__main__": 
    main()

"""
Another Way:
def is_valid(s):
    # Rule 1: Length must be 2–6 characters
    if not (2 <= len(s) <= 6):
        return False

    # Rule 2: Must start with at least two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    number_started = False
    for i, char in enumerate(s):
        if char.isdigit():
            if not number_started:
                # First number: make sure it's not '0'
                if char == "0":
                    return False
                number_started = True
        elif number_started:
            # A letter appeared after numbers started → invalid
            return False
        elif not char.isalnum():
            # Not a letter or number → invalid
            return False

    return True

"""