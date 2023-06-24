nums = []
for i in range(1,11):
  n = int(input("Enter a number to add to the list:"))
  nums.append(n)
greatest = nums[0]
for i in range(0, len(nums)):
  if(nums[i]>greatest):
    greatest = nums[i]
print("The biggest number in the list is:", greatest)