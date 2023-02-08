x = int(input("Insert number to take square root of: "))
iterations = int(input("How many iterations would you like: "))

def sqrtIter(x,iterations):
    y = (x+1)/2 # Initial guess
    for i in range(0,iterations):
        y = ((x/y) + y)/2
    print(y)
sqrtIter(x, iterations)