
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

countDownGoal2(7,1)