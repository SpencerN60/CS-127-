

def createList():
    newString = ""
    running = True
    newList = []
    while running:
        newString = input("Enter string to insert into list, enter * to finish list: ")
        if newString == "*":
            running = False
        else:
            newList.append(newString)
    return newList

def reverseList(list1):
    reversedList = []
    for i in list1:
        reversedList.insert(0,i)
    return reversedList

def main():
    normalList = createList()
    newList = reverseList(normalList)
    print("Is this list a palindrome?")
    if normalList == newList:
        print("True")
    else:
        print("False")

main()

