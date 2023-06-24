"""
A  
B C  
D E F  
G H I J  
K L M N O  
P Q R S T U  
V W X Y Z [ \ 
"""
a = 97

for i in range(0, 8):
  for j in range(0, i):
    c=chr(a) #ASCII values getting converted into Alphabets
    print(c, end=" ")
    a+=1
  print()