def isPrime(a:int):
  count = 0;
  for i in range(1, a+1):
    if(a%i == 0):
      count +=1;
  if(count > 2):
    return False
  else:
    return True

b = int(input("Enter a number and I will print all prime numbers that are less than the number:"))
for i in range(2, b+1):
  if(isPrime(i)):
    print(i)
