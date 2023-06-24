a = []
while(True):
  b = int(input("Enter random numbers. Enter 0 to stop"))
  if(b == 0):
    break
  else:
    a.append(b)
for i in range(0, len(a)-1):
  for j in range(0, len(a)-i-1):
    if(a[j]<a[j+1]):
      temp = a[j]
      a[j] = a[j+1]
      a[j+1] = temp
print(a)

#binary search an input in an unsorted array, sort the array first
#research selection sort