"""Calculate the sum and average of the digits present in a string"""

a = "Aarav 35"
sum = 0
length = 0
for i in range(1, len(a)):
  if(a[i].isdigit()):
    sum +=(int(a[i]))
    length+=1
average = sum/length
print("The average of the numbers inside this string is:", average)