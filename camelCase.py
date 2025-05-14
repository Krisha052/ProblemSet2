
def main():
    camel = input("camelCase: ")
    print(f"snake_case: {snake_case(camel)}")

def snake_case(s):
    result = ""
    for char in s:
        if char.isupper():
            result += "_" + char.lower()
        else:
            result += char
    return result

if __name__ == "__main__":
    main()
