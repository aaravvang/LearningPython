side_1 = float(input("Enter the first side of a triangle"))
side_2 = float(input("Enter the second side of a triangle"))
side_3= float(input("Enter the third side of a triangle"))
if((side_1== side_2) and (side_2 == side_3)):
  print("This triangle is equilateral.")
elif((side_1 == side_2) or (side_2 == side_3) or (side_1 == side_3)):
  print("This triangle is isosceles.")
elif((side_1 != side_2) and (side_2 != side_3) and (side_3 !=side_1)):
  print("This triangle is scalene.")