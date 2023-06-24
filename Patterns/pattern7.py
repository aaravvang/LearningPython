"""
        *
      # #
    * * *
  # # # #
* * * * *
"""
for i in range(0, 6):
  for j in range(5, i, -1):
    print(" ", end=" ")
  for k in range(0, i):
    if(i%2 == 0):
      print("#", end=" ")
    else:
      print("*", end=" ")
  print()