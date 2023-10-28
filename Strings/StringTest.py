
"""
Censor Words

You are given a list of forbidden words. Write a Python program that takes a string and replaces all occurrences of the forbidden words with "****". For example, if the forbidden words are ["bad", "ugly"], the string "This is a bad and ugly day" should become "This is a **** and **** day".
"""


story = input("How was your day?")
story = story.replace("bad", "***")
story = story.replace("ugly", "***")
story = story.replace("stupid", "***")
print(story)



"""
Remove File Extensions:
Given a string with a filename like "photo.jpg", write a Python program to remove the file extension, resulting in "photo".
"""
extension = input("What is your file extension called?")
files = extension.split(".")
print(files[0])



"""Extract Domain:
From an email address string, extract the domain name. For instance, from "john.doe@example.com", extract "example.com"."""
email = input("What is your email address?")
domains = email.split("@")
print("Username:", domains[0])
print("Domain name:", domains[1])


"""Reverse String:
Using slicing, reverse a string."""

word = input("Enter anything random and I will reverse it:")
rev=word[-1::-1]
print(rev)



"""
CSV to List:
Convert a string of comma-separated values into a list.
"""

String = input("Enter a csv sentence:")
words = String.split(",")
for i in range(0, len(words)):
  print(words[i])


"""
Check Protocol:
Check if a given URL starts with "https://". If it does, return "Secure", otherwise return "Not Secure".
"""
url = input("Enter a url, and I will see if it's safe:")
if("https" in url):
  print("Secure")
else:
  print("Not secure")