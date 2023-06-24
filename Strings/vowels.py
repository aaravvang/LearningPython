"""Write a program to remove all the vowels from a string."""
message = "Aarav Vangipuram"

vowel="aeiouAEIOU"
withoutVowel = ""

for i in message: #in keyword to stores each character of the message into i
  if(i not in vowel): 
    withoutVowel+=i
    
print(withoutVowel)
    
  