# month = int(input("Enter a month:"))
# day = int(input("Enter a day:"))
import datetime
d = datetime.datetime.now()
# days = int(d.strftime("%d"))
# daysBetween = day-days
# print("There are", daysBetween, "days between these 2 dates")


a=datetime.datetime(2023, 7, 15)
b=datetime.datetime(2023, 5, 15)
print(a-b)