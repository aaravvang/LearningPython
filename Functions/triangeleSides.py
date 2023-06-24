def TriangleSides(a:int, b:int, c:int):
  if((a==b) and (b==c)):
    return("Equilateral")
  elif((a == b) or (b==c) or (a==c)):
    return("Isosceles")
  elif((a!=b) and (b!=c) and (a!=c)):
    return("Scalene")
a1 = int(input("Enter a side of a triangle:"))
b1 = int(input("Enter a 2nd side of a triangle:"))
c1 = int(input("Enter a 3rd side of a triangle:"))
print("This triangle is:", TriangleSides(a1,b1,c1))