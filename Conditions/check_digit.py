num = float(input("Enter your number:"))
if(num>-10 and num<10):
  print("This number is a single digit number.")
elif((num>=10 and num<100) or (num<=-10 and num>-100)):
  print("This number is a two digit number")
elif((num>=100 and num<1000) or (num<=-100 and num>-1000)):
  print("This number is a three digit number.")
else:
  print("This number isn't a one, two, or three digit number.")
