"""Create a class called TimeConverter with a method called convert(). Implement method overloading for the convert() method to allow converting time from hours and minutes to seconds or from seconds to hours and minutes."""
class TimeConverter:
  def __init__(self):
    self.time = ""
  def convert(self, hr=0,min=0,sec=0):
    if(hr>0 or min>0):
      sec = (hr*3600)+(min*60)
      self.time = f"{sec} Seconds"
    else:
      hours = sec//3600
      sec-=(hours*3600)
      mins = sec/60
      self.time = f"{hours} Hours and {mins} Minutes"
      
    return self.time
    
Time = TimeConverter()
print(Time.convert(0,0,18240))











#   306
    # 306/100=3 
    # 3*100=300
    # 306-300=6
