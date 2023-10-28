"""Create a program that reads a text file named "story.txt" and counts the number of lines, words, letters in it. Print the count to the console."""
message = ""
try:
   with open("File_IO/txt_files/story.txt") as reader:
    message = reader.read()
    print(reader.readline())
except:
  print("Error reading file.")
  
print(message)

print("Length of the story:", len(message))
messages = message.split(" ")
lines = message.split("\n")
print("The number of words in this story is:" ,len(messages))
print("The number of lines in this story is:", len(lines))


