'''Write a program to accept the total shopping amount and give the discount according the following criteria: Below $7000 give 10% discount, if its greater than $7000 and less than $10000, give a 15% discount. If it's greater than $10000, give a 20% discount'''


total_amount = int(input("Enter the total amount of the billing:"))
if(total_amount<= 7000):
  print("You'll have a discount of 10%")
  discount = 7000*0.1
  print("Your discount is:", discount)
  new_amount = total_amount - discount
  print("Your new total is:$", new_amount)
elif((total_amount<10000)):
  print("You'll have a discount of 15%")
  discount = 7000*0.15
  print("Your discount is:", discount)
  new_amount = total_amount - discount
  print("Your new total is: $", new_amount)
elif(total_amount >=10000):
  print("Your discount is 20%")
  discount = 7000*0.2
  print("Your discount is:", discount)
  new_amount = total_amount - discount
  print("Your new amount is:$", new_amount)
else:
  print("Please enter another amount.")