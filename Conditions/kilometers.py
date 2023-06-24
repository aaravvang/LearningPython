kilometers = int(input("Enter the amount of kilometers you drove:"))
if(kilometers<=10):
  price = kilometers * 11
  
elif(kilometers<=100):
  price = 110 + (kilometers-10)*10
elif(kilometers>100):
  price = 110 + 900 +(kilometers - 100)*9
print("Your total price is:$", price)