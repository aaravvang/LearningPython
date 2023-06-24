"""Create a class named Time with properties hours, minutes, and seconds. Add a method total_seconds() that calculates and returns the total number of seconds."""
class Time:
  hours = 0 #instance va
  mins = 0
  secs = 0
  def input(self):
    self.hours = int(input("Enter a number of hours:"))
    self.mins = int(input("Enter a number of mins:"))
    self.secs = int(input("Enter a number of secs:"))
  def total_seconds(self):
    totalSeconds = (self.hours * 3600)+(self.mins*60)+self.secs
    return totalSeconds
   
time = Time()
time.input()
print(time.total_seconds())