import Strings
a = "Aarav"
reverseString = " "
for i in range(1, len(a)+1):
  reverseString = reverseString + a[len(a) - i]
print(reverseString)