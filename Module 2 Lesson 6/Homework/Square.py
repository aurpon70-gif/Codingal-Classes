import turtle
turtle.Screen().bgcolor("aqua")
turtle.Screen().setup(500,500)
square = turtle.Turtle()

for i in range(0, 4):
    square.forward(100)
    square.right(90)

turtle.done()