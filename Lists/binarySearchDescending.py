num = [10,9,8,7,6,5,4,3,2,1]
a = int(input("Enter a number that's in this list:"))
start = 0
end = len(num)-1
isFound = False
while(start<=end):
  mid = int((start+end)/2)
  if(num[mid] == a):
    print("Your number is in the list and the index is:", mid+1)
    isFound = True
    break
  elif(num[mid]<a):
    end = mid-1
  elif(num[mid]>a):
    start = mid+1
if(isFound == False):
  print("Your number isn't in this list")