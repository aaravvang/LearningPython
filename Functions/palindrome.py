def palindrome(num: int):
  num2 = num
  reverse = 0
  while(num>0):
    last_digit = num%10
    reverse = (reverse*10)+last_digit
    num = int(num/10)
  if(reverse == num2):
    return True
  else:
   return False
a = int(input("Enter a number:"))
print(palindrome(a))