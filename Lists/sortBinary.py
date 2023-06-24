a = [4,3,5,2,13,6,7,1,56,9,10]
b = int(input("Enter a number to find in this unsorted array, I will tell you if it's there:"))

for i in range(0, len(a)-1):
  for j in range(0, len(a)-i-1):
    
    if(a[j]>a[j+1]):
        temp = a[j]
        a[j] = a[j+1]
        a[j+1] = temp
 
start = 0
end = len(a)-1
isFound = False
while(start<=end):
  mid = int((start+end)/2)
  
  if(a[mid]==b):
    print("Your number is in the list")
    isFound = True
    break
  elif(a[mid]<b):
    start = mid+1
  else:
    end = mid-1
if(isFound == False):
  print("Your number isn't in the list")
