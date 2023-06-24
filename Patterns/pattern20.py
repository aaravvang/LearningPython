"""
1 
2 3 4 
5 6 7 8 9
"""
counter = 1
for i in range(0, 4):
  for j in range(0, i+(i-1)):
    print(counter, end=" ")
    counter+=1
  print()