import random



def numberedList(list):
    numberedList = []
    for i in range(0,len(list)):
        numberedList.append(i)
    return numberedList

def stringList():
    string = input("Please input a string: ")
    list1 = string.split() 
    return list1

def main():
    dist = {}
    valueList = []
    initialList = stringList()
    listCopy = initialList.copy()
    for i in initialList:
        choice = random.choice(listCopy)
        dist[i] = choice
        listCopy.remove(choice)
    print(initialList)
    print(dist) 
    for values in dist.values():
        valueList.append(values)
    finalString = ""
    for i in valueList:
        finalString += i + " "
    print(finalString)
        


if __name__ == "__main__":
    main()
























