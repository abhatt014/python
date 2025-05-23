# Task 1: Perform Basic Mathematical Operations
# Write a Python program that does the following: 
#   1. Takes two numbers as input from the user.
#   2. Performs the basic mathematical operations on these two numbers: 
#       Addition
#       Subtraction
#       Multiplication
#       Division
#   3. Displays the results of each operation on the screen.
# Expected Output: (Assuming user enters 5 and 10) 
#   Enter the first number: 5
#   Enter the second number: 10
#   Addition: 15
#   Subtraction: -5
#   Multiplication: 50
#   Division: 0.5

# input 2 numbers
num1 = int(input("Enter 1st number"))
num2 = int(input("Enter 2nd number"))

#perform operations
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

#display results
print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mul}")
print(f"Division: {div}")

