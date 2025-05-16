# Data Structures and Strings in Python
# Task 1: Create a Dictionary of Student Marks
# Problem Statement: Write a Python program that: 
#   1.	Creates a dictionary where student names are keys and their marks are values.
#student_marks_dict = {"Alice": 85,"Bob": 92,"Charlie": 78,"Diana": 95,"Eva": 88 }
#   2.	Asks the user to input a student's name.
#   3.	Retrieves and displays the corresponding marks.
#   4.	If the student’s name is not found, display an appropriate message.
# Expected Output: 
# If user enters "Alice" (and Alice is in the dictionary): 
# Enter the student's name: Alice
# Alice's marks: 85
# If user enters "John" (and John is not in the dictionary): 
# Enter the student's name: John
# Student not found.

# input username
name = input("Enter the student's name: ")
name = name.capitalize()


#create dictionary
student_marks_dict = {"Alice": 85,"Bob": 92,"Charlie": 78,"Diana": 95,"Eva": 88 }

#check
if name in student_marks_dict:
    print(f"{name}'s marks: {student_marks_dict[name]}")
else:
    print("Student not found.") 

    