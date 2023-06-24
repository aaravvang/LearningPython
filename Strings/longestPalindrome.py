message = input("Enter random palindromes:")
splitMessage = message.split(" ")
isPalindrome = True
start = 0
end = len(splitMessage)-1
for i in range(0, len(splitMessage)):
  greatest = splitMessage[0]
  if(splitMessage[0]>greatest):

