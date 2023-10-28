import turtle
x = turtle.Turtle()
for i in range(100, 49, -10):
  for j in range(0,2):
    x.forward(i)
    x.left(90)
    x.forward(i/2)
    x.left(90)