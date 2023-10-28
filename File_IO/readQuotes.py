'''Create a program that reads the content of a text file named "quotes.txt" and prints each quote in uppercase.'''
try:
  with open("File_IO/txt_files/quotes.txt") as reader:
    message = reader.read()
except:
  print("Error reading file")

quotes = message.split("\n")
for i in range(0, len(quotes)):
  quotes[i] = quotes[i].upper()
  print(quotes[i])
