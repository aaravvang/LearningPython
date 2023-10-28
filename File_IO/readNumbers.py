try:
  with open("File_IO/txt_files/numbers.txt") as reader:
    numbers = reader.read()
except:
  print("Error reading file")

numbers = numbers.split("\n")
sum=0
for i in range(0, len(numbers)):
  numbers[i] = int(numbers[i])
  sum+=numbers[i]
print("The sum of these numbers is:", sum)