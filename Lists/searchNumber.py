nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,51,62,73,74,85,86,97,98,99,110]
count=0
a = int(input("Which number do you want to search in the list:"))
found = False
for i in range(0, len(nums)):
  count+=1
  if(a == nums[i]):
    found=True
    break
if(found==True):
  print("This number is in the list")
else:
  print("Your number isn't found.")
  
print("No of Iterations", count)

#Binary Search
count=0

start = 0
end = len(nums)-1
isFound = False
while(start<=end):
  mid = int((start+end)/2)
  count+=1
  if(nums[mid]==a):
    print("Your number is in the list")
    isFound = True
    break
  elif(nums[mid]<a):
    start = mid+1
  else:
    end = mid-1
if(isFound == False):
  print("Your number isn't in the list")
print("No of Iterations", count)
  


  