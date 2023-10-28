#write a python code to read a txt file for a number and check if it is palindrome or not
def palindrome(message):
  messages = message 
  reverse = 0
  while(message>0):
    last_digit = message%10
    reverse = (reverse*10)+last_digit
    message = int(message/10)
  if(reverse == messages):
    print(messages,"is a palindrome")
  else:
    print(messages,"is not a palindrome")


message = 0
try:
  with open("File_IO/txt_files/palindrome.txt") as file_object:
    message=file_object.read()
except:
  print("There was an error in reading the file")
  



list = message.split(",")
for i in range(0, len(list)):
  palindrome(int(list[i]))