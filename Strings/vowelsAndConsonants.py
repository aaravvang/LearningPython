"""Write a program to count vowels and consonants in a string."""

a = "Aarav"
v = 0
c = 0
a = a.lower()
for i in range(0, len(a)):
  # if(a[i] == "a" or a[i] == "e" or a[i] == "i" or a[i] == "o" or a[i] == "u"):
  if(a[i] in ['a','e','i','o','u']):
    v+=1
  else:
    c+=1
print("# of vowels:", v)
print("# of consonants:", c)