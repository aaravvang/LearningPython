import turtle
x=turtle.Turtle()
x.shape("turtle")
x.fillcolor("red")
x.begin_fill()
for i in range(0,4):
  x.forward(100)
  x.right(90)
x.end_fill()
