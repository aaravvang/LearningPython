num = int(input("Enter a number:"))
product = 1
while(num>0):
  last_digit = num%10
  product = product * last_digit
  num = int(num/10)
print(product)