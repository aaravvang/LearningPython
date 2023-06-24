def leapYearChecker(a:int):
  if(a%4 == 0):
    print("This year is a leap year")
  else:
    print("This year isn't a leap year")
b = int(input("Enter a year:"))
leapYearChecker(b)