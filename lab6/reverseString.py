
def main():
    var = input("Insert string: ")
    finalString = reverseString(var)
    print(finalString)

    


def reverseString(string):
    reverse = ""
    for i in string:
        reverse = i + reverse
    return reverse





if __name__ == "__main__": 
    main()




