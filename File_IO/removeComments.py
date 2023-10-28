"""Remove Comments:
Given a Python source code file, write a program that removes all comments (lines starting with #) and saves the cleaned code to a new file."""

try:
  with open("File_IO/txt_files/comments.txt") as reader:
    messages = reader.read()
except:
  print("Error reading file")

message = messages.splitlines()
print(messages)
newstr = ""
for i in message:
  line=i.split("#")
  newstr = newstr +line[0] +"\n"


with open("File_IO/txt_files/comments.txt", "w") as writer:
  writer.write(newstr)

