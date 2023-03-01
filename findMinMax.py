

def createList():
    list1 = []
    var = 0
    running = True
    while running:
        var = input("Enter number to add to list, enter * to quit: ")
        if var == "*":
            running = False
        else:
            list1.append(int(var))
    return list1

def findMin(list1):
    minimum = list1[0]
    for i in list1:
        if i < minimum:
            minimum = i
    return minimum

def findMax(list1):
    maximum = list1[0]
    for i in list1:
        if i > maximum:
            maximum = i
    return maximum


def main():
    list2 = createList()
    mini = findMin(list2)
    maxi = findMax(list2)
    print("The list is {}".format(list2))
    print("The minimum in this list is {}".format(mini))
    print("The maximum in this list is {}".format(maxi))

if __name__ == "__main__":
    main()




