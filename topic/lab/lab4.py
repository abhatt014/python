# Task 2: Sum of Integers from 1 to 50 Using a Loop
# Problem Statement: Write a Python program that: 
#   1.	Uses a for loop to iterate over numbers from 1 to 50.
#   2.	Calculates the sum of all integers in this range.
#   3.	Displays the final sum.
# Expected Output: 
#   The sum of numbers from 1 to 50 is: 1275

# input from user
sum = 0
last_num = int(input("Enter the last num: "))
last_num = last_num + 1 
for num in range(1, last_num):
    sum = sum + num

print(f"The sum of numbers from 1 to {last_num - 1} is: {sum}")

