def highestNumber():
  a = [2, 3, 98, 9]
  counter = a[0];
  for i in range(1, len(a)):
    if(a[i]>counter):
      counter = a[i]
  print("The largest number is:", counter)
highestNumber()
  