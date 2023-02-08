import random

# get inputs
a = int(input("Insert integer 1: "))
b = int(input("Insert integer 2: "))
c = int(input("Insert number of interations: "))

def randomSum(a,b,c): # define function
    sum = 0
    for i in range(0, c):
        sum += random.randrange(a,b+1)
    print("The sum of the {} numbers from {} to {}, is {}".format(str(c), str(a), str(b), str(sum)))


randomSum(a,b,c) # call function