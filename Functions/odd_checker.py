def oddChecker(a:int):
  if(a%2 != 0):
    return True
  else:
    return False


num = int(input("Enter a number, and I will check if it's odd or not:"))
print(oddChecker(num))