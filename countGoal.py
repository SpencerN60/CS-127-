
def countDownGoal(n,goal):

    if n < goal:
        return
    countDownGoal(n,goal+1)
    print(goal)




def countDownGoal2(n,goal):
    if n < goal:
        return
    print(n)
    countDownGoal(n-1,goal)

def main():
    n = int(input("What number would you like to start at: "))
    goal = int(input("What is your goal number: "))
    countDownGoal(n,goal)
    print("----------------------")
    countDownGoal2(n,goal)

if __name__ == "__main__":
    main()