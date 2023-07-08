import turtle
n = int(input("Enter the number of sides you want:"))
x = turtle.Turtle()
x.fillcolor("#000000")

angle = (180*(n-2))/n
turtleAngle = 180-angle
x.begin_fill()
for i in range(0,n):
  x.forward(50)
  x.left(turtleAngle)
x.end_fill()