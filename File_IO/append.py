try:
  with open("File_IO/txt_files/thecyper.txt","a") as reader:
    messages = reader.write("This is a new line")
except:
  print("Error reading file.")