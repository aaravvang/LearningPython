a = "   eve               "
# count = 0
# for i in range(0, int((len(a))/2)):
#   if(a[i] == a[(len(a)-1)-i]):
#     count+=1
# if(count == int(len(a)/2)):
#   print("This string is a palindrome")
# else:
#   print("This string isn't a palindrome")
a=a.strip()
isPalindrome=True
start=0
end=len(a)-1
while(start<=end):
  if(a[start]==a[end]):
    start+=1
    end-=1
  else:
    isPalindrome=False
    break

if(isPalindrome==True):
  print("This string is a palindrome")
else:
  print("This string isn't a palindrome")

for x in a:#loop to cycle through a string
  print(x)