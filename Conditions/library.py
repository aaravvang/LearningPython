'''Accept the number of days from the user and calculate the charge for library according to following :

Till five days : $ 2/day.

Six to ten days  : $ 3/day.

11 to 15 days  : $ 4/day

After 15 days    : $ 5/day'''


days = int(input("Enter the amount of days your book has been not returned for after the due date:"))
if(days<= 5):
  price = days * 2
elif(days<=10):
  price = 10 +(days - 5)*3
elif(days<=15):
  price = 10 + 15 + (days-10)*4
elif(days>15):
  price = 10+15+20+(days - 15)*5
print("Your total charge for the days after the due date is:$", price)


'''
13

first 5 day = 5*2=10
next 5 days = 5*3=15
next 3 days = 3*4=12'''