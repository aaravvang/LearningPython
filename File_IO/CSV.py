message = ""
try:
  with open("File_IO/txt_files/csv.txt") as reader:
    message = reader.read()
except:
  print("Error reading file")
words = message.split(",")
for i in range(0, len(words)):
  print(words[i])