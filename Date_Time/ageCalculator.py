import datetime
d = datetime.datetime.now()
year = int(input("What year were you born?"))
curYear = d.strftime("%Y")
curYear = int(curYear)
print("Your age is:", curYear-year)