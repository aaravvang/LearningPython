"""
0
1 1
2 3 5
8 13 21 34
55 89 144 233 377
"""

x=0
y=1

for i in range(1,6): #Pattern code
  for j in range(0, i):
    z=x+y
    temp = x
    x = y
    y = temp+y
    print(temp,end=" ")
   
  print()

