"write a pyhton code that re-writes a file"


with open("File_IO/txt_files/test.txt","w") as writer:
  writer.write("this file was written by an alien") #write function rewrites the message if the file already exist
  
writer.close()
print("done.")