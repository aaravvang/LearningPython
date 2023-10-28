#write a code to print the time now
import datetime
d = datetime.datetime.now()
hour = int(d.strftime("%H"))
mins = int(d.strftime("%M"))
print("The time is:", hour, ":", mins)