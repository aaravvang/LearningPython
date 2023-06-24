"""
*****
*   *
*   *
*   *
*****
"""
rows = int(input("Enter the number of rows you want:"))
for i in range(0, rows):
  for j in range(0, rows):
    if((i == 0) or (i==rows-1)):
      print("*", end="")
    else:
      if((j==0) or (j==rows-1)):
        print("*", end="")
      else:
        print(" ", end="")
  print()
      
      
      
     
  