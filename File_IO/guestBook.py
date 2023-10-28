'''Guest Book: You're creating a guest book for an event. Write a Python program that allows guests to input their names and comments. Append each guest's name and comment to a file. Ensure that the comments of different guests are separated by a line break.'''
print("Enter the reservations, click on one to quit.")
while(1<2):
  names = input("Enter your name and comments (enter -1 to quit):")
  if(names == "-1"):
    break
  with open("File_IO/txt_files/guestBook.txt", "a") as writer:
    writer.write(names)
    writer.write("\n")
    