"""
    1
   212
  32123
 4321234
543212345
"""
temp=0
for i in range(0, 6):
  for j in range(5, i, -1):
    print(" ", end="")
  for k in range(i, 0, -1):
    print(k, end="")
    temp=k
  for l in range(temp+1, i+1):
    print(l, end="")
  
  print()