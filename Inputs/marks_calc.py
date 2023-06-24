#Write a python code to take input of marks in 5 subjects and print the total and the average.

english_grade = float(input("How much marks did you get in English?:"))
math_grade = float(input("How much marks did you get in Math?:"))
science = float(input("How much marks did you get in Science?:"))
history = float(input("How much marks did you get in History?:"))
french = float(input("How much marks did you get in French?:"))
total_grade = english_grade + math_grade+science+history+french

average = (total_grade)/5

print("Your total marks for the 5 subjects is:", total_grade)

print("Your average marks for each subject is:", average)
full_marks = 250
percentage = ((total_grade)/full_marks)*100

print("Your percentage grade is:", percentage, "%")



