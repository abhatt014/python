# Task 2: Using the Math Module for Calculations
#   Problem Statement: Write a Python program that: 
#   1.  Asks the user for a number as input.
#   2.	Uses the math module to calculate the: 
#           Square root of the number
#           Natural logarithm (log base e) of the number
#           Sine of the number (in radians)
#   3.  Displays the calculated results.
# Expected Output: (For user input 25) 
# Enter a number: 25
# Square root: 5.0
# Logarithm: 3.2188758248682006
# Sine: -0.13235175009777303

#import math module
import math as m
# input number
num = int(input("Enter a number: "))

#calculate
sqrt = m.sqrt(num)
log = m.log(num)
sin = m.sin(num)

#display    
print(f"Square root: {sqrt}")
print(f"Logarithm: {log}")
print(f"Sine: {sin}")