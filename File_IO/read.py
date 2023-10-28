try:
  with open("File_IO/txt_files/hello.txt") as file_object:
    message=file_object.read()
    print(message)
except:
  print("There was an error")