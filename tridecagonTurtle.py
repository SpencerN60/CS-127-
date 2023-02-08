import turtle
# https://mathworld.wolfram.com/Tridecagon.html


s = int(input("Length of sides: "))
x = int(input("X coordinate of vertex: "))
y = int(input("Y coordinate of vertex: "))

def tridecagonTurtle(s,x,y):
    wb = turtle.Screen()
    wb.bgcolor("black")
    spencer = turtle.Turtle()
    spencer.color("yellow")
    spencer.penup()
    spencer.setpos(x,y)
    spencer.pendown()
    for i in range(0,13):
        spencer.forward(s)
        spencer.left(360/13)
    wb.exitonclick()

tridecagonTurtle(s,x,y)
