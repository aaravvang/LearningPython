"""Create a string made of the middle three characters"""
a = input("Enter a string:")
b = a[int(len(a)/2)]
c = a[int(len(a)/2)-1]
d = a[int(len(a)/2)+1]
print(c+b+d)