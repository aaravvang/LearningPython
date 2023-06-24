"""Create a string made of the first, middle and last character"""
a = input("Enter a string:")
first = a[0]
middle = a[(int(len(a)/2))]
last = a[len(a)-1]
print(first+middle+last)