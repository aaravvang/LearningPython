"""Write a simple program that reads a file and encrypts its content by shifting each character by a fixed number (e.g., Caesar cipher) and then saves the encrypted content to a new file

example - 
abcd
97+5=102>e
98+5=103>f
99>g
100>h

efgh
"""
messages = ""
shift = 5
try:
  with open("File_IO/txt_files/thecyper.txt") as reader:
    messages = reader.read()
except:
  print("Error reading file.")

encrypted=""
for i in range(0, len(messages)):
  charac = ord(messages[i])
  shifted = charac+shift
  encrypted = encrypted+ chr(shifted)



with open("File_IO/txt_files/cyphered.txt", "w") as writer:
  writer.write(encrypted)

print("done")


