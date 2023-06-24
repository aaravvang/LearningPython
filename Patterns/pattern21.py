"""
10 
10 8 
10 8 6 
10 8 6 4 
10 8 6 4 2
"""
for i in range(0,6):
  count=10
  for j in range(0,i):
    print(count, end=" ")
    count-=2
  print()