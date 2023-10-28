"""Write a python code that creates a new file named test.txt and insert the text into it as 'this message is written by python' """

with open("File_IO/txt_files/test.txt","w") as writer:
  writer.write("this message is written by python.") #write function helps writing the message in the newly created file

  writer.write("\nthis is a second line") #inserts a new line
writer.close()
print("done")