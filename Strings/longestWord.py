"""Write a program to find the length of the longest word in a string."""
message = "Write a program to find the length of the longest word in a string"

List = message.split(" ")
longest = List[0]
for i in List:
  if(len(i)>len(longest)):
    longest = i
print("The longest word in the message is:", longest)