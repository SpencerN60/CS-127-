import reverseString

def main():
    var = input("Input string you want to check: ")
    reverse = reverseString.reverseString(var)
    if reverse == var:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")

if __name__ == "__main__":
    main()