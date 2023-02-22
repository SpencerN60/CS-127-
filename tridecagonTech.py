
import turtle
import oldTri
import random

def createLSystem(numIters,axiom): #1
    startString = axiom # F
    endString = ""
    for i in range(numIters): # This is done 4 times
        endString = processString(startString)
        startString = endString

    return endString

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr

def applyRules(ch):
    newstr = ""
    if ch == 'F':
        newstr = 'F-F++T-F'   # Rule 1
    elif ch == "T":
        newstr = "F-P-T+F"
    elif ch == "P":
        newstr = "T-P-F+F"
    else:
        newstr = ch    # no rules apply so keep the character

    return newstr

def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == "T":
            oldTri.tridecagonTurtle(aTurtle)
        elif cmd == "P":
            aTurtle.penup()
            aTurtle.setpos(random.randint(-250,250), random.randint(-250,250))
            aTurtle.pendown()
        

def main():
    inst = createLSystem(4, "TPFFFPPT")   # create the string
    print(inst)
    t = turtle.Turtle()            # create the turtle
    wn = turtle.Screen()

    t.up()
    t.back(200)
    t.down()
    t.speed(20)
    drawLsystem(t, inst, 60, 20)   # draw the picture
                                  # angle 60, segment length 5
    wn.exitonclick()

main()
