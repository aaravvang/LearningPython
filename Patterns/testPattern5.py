"""
    1
   1 2
  1   3
 1     4
1 2 3 4 5
"""
for i in range(0,6):
  for j in range(5, i, -1):
    print(" ", end="")
  for k in range(1, i+1):
    if((i==0) or (i == 5)):
      print(k, end=" ")
    else:
      if((k == 1) or (k == i)):
        print(k, end=" ")
      else:
        print(" ", end=" ")
    
  print()