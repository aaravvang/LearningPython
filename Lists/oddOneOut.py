num = []
print("Enter an element into the list. Every element should be in the list thrice, but also add an odd one out.(Enter -1 to stop")
while(True):
  
  a = int(input("Enter a number:"))
  if(a == -1):
    break
  else:
    num.append(a)

ans = 0
for i in range(0, len(num)):
  
  ans = ans ^ num[i]
  if((ans ^ num[i]) == 1):
    
print(ans)
  