"""
1
3 2
6 5 4
10 9 8 7
"""
start=1
stop=1
for i in range(1, 5):
  for j in range(start, stop-1, -1):
    print(j, end=" ")
  stop = start+1
  start = stop+i
  print()