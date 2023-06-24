a = int(input("Enter your baby's age:"))

if(a<=3):
  b = int(input("Enter your baby's height:"))
  if(b<24):
    print("This baby is eligible to get a baby ticket.")
  else:
    print("This baby is too tall for a baby ticket.")
else:
  print("Your baby is too old for a baby ticket.")