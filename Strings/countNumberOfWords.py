message = input("Enter some random words:")
splitMessage = message.split(" ")
count = 0
for i in splitMessage:
  count+=1
print("Number of words in your message: ", count)