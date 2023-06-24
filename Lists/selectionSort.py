a = [5,6,1,4,2,10,9,11,26,19,68]
for i in range(0, len(a)):
  minIndex = i
  for j in range(i, len(a)):
    if(a[j]<a[minIndex]):
      minIndex = j
  temp = a[i]
  a[i] = a[minIndex]
  a[minIndex] = temp
print(a)
