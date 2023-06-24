import random


# function
def check(user, comp):
  
  if(user == comp):
    return 0
  if(user==1 and comp == 2):
    return -1
  elif(user==2 and comp == 3):
    return -1
  elif(user == 3 and comp == 1):
    return -1
  else:
    return 1
    

#driver code
score = 0
compscore = 0
while(1<2):
  user = int(input("\n Enter a 1, 2, or 3. They stand for rock, paper, and scissor respectively:"))
  
  if(user==-1):
    print("Bye")
    break # breaking the loop
  if(user>3 or user<=0):
    print("Invalid input")
    continue #skipping to the next iteration
    
    
  comp = random.randint(1,3)
  option=["Rock","Paper","Scissor"] #array
  print("User picked:",option[user-1])
  print("Computer picked:", option[comp-1])
  
  
  result = check(user,comp) #function calling
  
  if(result == 0):
    print("Draw")
  elif(result == -1):
    compscore+=1
    print("You lose!")
  else:
    score+=1
    print("You win!")
  print("Your score is:", score)
  print("The computer's score is:", compscore)
  
