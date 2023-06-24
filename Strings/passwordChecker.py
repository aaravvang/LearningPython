import Strings
'''
8 digits or more, 1 special character, 1 captial letter, 1 small letter, and one number
'''
isSpecial = False
isCaptial = False
isSmall = False
isDigit = False
a = input("Enter a password:")
if(len(a)<8):
  print("This isn't a strong pasword")

else:
  for i in range(0, len(a)):
    
    if((a[i]).isdigit()):
      isDigit = True
    elif(a[i].isupper()):
      isCaptial = True
    elif(a[i].islower()):
      isSmall = True
    else:
      isSpecial = True
  if(isDigit == True and isCaptial == True and isSpecial == True and isSmall == True):
    print("This is a good password good job")
  else:
    print("This isn't a strong password")
    
    

