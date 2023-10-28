'''Write a program that reads the first line from a text file named "intro.txt" and prints it.

Write a program that reads the second line from a text file named "intro.txt" and prints it.'''
try:
  with open("File_IO/txt_files/intro.txt") as reader:
    messages = reader.read()
except:
  print("Error reading file")

lines = messages.splitlines()
print("The first line is:", lines[0])
print("The second line is:", lines[1])
