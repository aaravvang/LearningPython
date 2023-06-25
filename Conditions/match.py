a = input("Enter a number:")

match (a):#assigning a as the match key
  case 'checkbal': print("This is the 1st option")

  case 'e': print("Exited")

  case _: print("this is the wrong input, try again") #default case
  
  