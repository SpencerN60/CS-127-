import turtle
# https://mathworld.wolfram.com/Tridecagon.html




def tridecagonTurtle(t):
    
    t = turtle.Turtle()
    t.color("yellow")
    t.penup()
    t.setpos(0,0)
    t.pendown()
    for i in range(0,13):
        t.forward(50)
        t.left(360/13)
    


