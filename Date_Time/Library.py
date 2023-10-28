# The Head Librarian at a library wants you to make a program that calculates the fine for returning the book after the return date. You are given the actual and the expected return dates. Calculate the fine as follows:

#   a. If the book is returned on or before the expected return date, no fine will be charged, in other words fine is 0.
#   b. If the book is returned in the same month as the expected return date, Fine = 15 Rupees × Number of late days
#   c. If the book is not returned in the same month but in the same year as the expected return date, Fine = 500 Rupees × Number of late months
#   d. If the book is not returned in the same year, the fine is fixed at 10000 Rupees.


import datetime

d = datetime.datetime.now()
fine=0
month = int(input("What month did you return the book?"))
yr = int(input("Year?"))
day = int(input("Day?"))

today_day=int(d.strftime("%d"))
today_month=int(d.strftime("%m"))
today_year = int(d.strftime("%Y"))


if(yr>today_year):
  fine=10000
elif(month>today_month):
  fine = 500*(month-today_month)
 
elif(day>today_day):
  fine = 15*(day-today_day)
  
print("Your fine is $",fine)