"""Print a reverse pyramid"""

for i in range(0, 6):
  for j in range(0, i):
    print(" ", end="")
  for k in range((6-i), 0, -1):
    print("# ", end="")
  print()