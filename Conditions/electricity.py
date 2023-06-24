'''First 100 units ~ $5/Unit
next 100 units ~ $6/unit
next 50 units ~ $7/unit
next 25 units ~ $8/unit
next 25 units ~ $9/unit
Above units ~ $10/unit'''

Units = int(input("Enter the amount of Kilowatts of electricity you used this day:"))
if(Units<=100):
  price = Units * 5
elif(Units<=200):
  price = 500 +(Units-100)*6
elif(Units<=250):
  price = 500+600+(Units-200)*7
elif(Units<=275):
  price = 500+600+350+(Units-250)*8
elif(Units<=300):
  price = 500+600+350+200+(Units-275)*9
elif(Units>300):
  price = 500+600+350+200+225+(Units-300)*10
print("Your total price is:$", price)
