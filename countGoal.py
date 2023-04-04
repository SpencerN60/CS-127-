

def countDownGoal(n,goal):
    while n >= goal:
        print(n)
        n -= 1


def main():
    n = int(input("Pick a starting number"))
    goal = int(input("Pick a goal"))
    countDownGoal(n,goal)

