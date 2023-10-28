"""
Password Manager: Build a simple password manager that allows users to store and retrieve passwords for different accounts. Passwords should be saved securely in a file. Users can add new passwords, view saved passwords, and search for a specific account's password.
"""

def search(p, acct):
  for i in p:
    line=i.split(":")
    if(line[0]==acct):
      return(line[1])


    # if(i.startswith(acct)):
    #   result=i.split(":")
    #   return(result[1])


while(True):
  o = int(input("Enter 1 to enter a password, enter 2 to view passwords, and 3 to search for a specific password, or -1 to exit:"))
  if(o == -1):
    print("bye")
    break
  if(o == 1):
    a = input("Enter a password in this format(Account : password):")
    with open("File_IO/txt_files/passswords.txt", "a") as writer:
      writer.write(a)
      writer.write("\n")
  if(o == 2):
    with open("File_IO/txt_files/passswords.txt") as reader:
      passwords = reader.read()
    password = passwords.split("\n")
    for i in range(0, len(password)):
      print(password[i])
  if(o == 3):
    with open("File_IO/txt_files/passswords.txt") as reader:
      passwords = reader.read()
    password = passwords.split("\n")
    # for i in range(0, len(password)):
    #   eachPass = password.split(":")
    acct = input("What account do you want the password for?")
    print(search(password, acct))


