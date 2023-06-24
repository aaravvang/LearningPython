"""Print a diamond"""
for i in range(0,7):
  for j in range(6, i, -1):
    print(" ", end="")
  for k in range(0, i):
    print("# ", end="")
  print()
for l in range(0,6):
  for o in range(0, l):
    print(" ", end="")
  for n in range((6-l), 0, -1):
    print("# ", end="")
  print()