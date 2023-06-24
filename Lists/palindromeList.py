nums = []
size = int(input("Enter the size of the array you want:"))
for i in range(1,size+1):
  n = int(input("Enter a number to add to the list:"))
  nums.append(n)

isPalin = True
for i in range(0, int(len(nums)/2)):
  if(nums[i] != nums[len(nums)-(i+1)]):
    isPalin=False
    break
if(isPalin == False):
  print("This list isn't a palindrome list")
else:
  print("This list is a palindrome list")

