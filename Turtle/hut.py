import turtle
x = turtle.Turtle()
x.goto(-100,0)
for i in range(0,4):
  x.forward(100)
  x.right(90)

x.left(60)
for i in range(0,3):
  x.forward(100)
  x.right(120)

x.penup()
x.forward(100)
x.right(60)
x.pendown()
x.forward(200)
x.right(60)
x.forward(100)
x.right(120)
x.forward(200)
x.penup()
x.left(90)
x.forward(100)
x.left(90)
x.pendown()
x.forward(200)
x.left(90)
x.forward(100)

