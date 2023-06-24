import Strings
a = input("Enter some words:")
"""b={}
b.append(a[0])
for i in range(0, len(a)):
  if(a[i] == " "):
    b.append(a[i]+1)
print(b)"""
ans=''
b=a.rsplit(" ")
print(b)
for i in range(0, len(b)):
  word=b[i]
  ans=ans+word[0]
print(ans)