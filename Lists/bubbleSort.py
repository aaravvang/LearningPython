a = []
while(True):
  b = int(input("Enter random values into a list. Enter 0 to stop:"))
  if(b == 0):
    break
  else:
    a.append(b)
# count_i = 0
# count_j = 0
for i in range(0, len(a)-1):
  # count_i=count_i+1
  # count_j=0
  for j in range(0, len(a)-i-1):
    # count_j=count_j+
    if(a[j]>a[j+1]):
      #Swapping
        temp = a[j]
        a[j] = a[j+1]
        a[j+1] = temp
  # print(count_i, count_j)
print(a)

        
      
    