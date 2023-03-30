# -*- coding: utf-8 -*-
"""Programming Assignment_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jvXcVGNq7NxOyBk1BDWnJqBUzs2kzhNz

## Programming Assignment_4
----------------

### 1. Write a Python Program to Find the Factorial of a Number?
"""

# Get the number from the user
num = int(input("Enter a number: "))

# Initialize the factorial variable to 1
factorial = 1

# Compute the factorial of the number
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)

"""### 2. Write a Python Program to Display the multiplication Table?"""

# Get the number from the user
num = int(input("Enter a number: "))

# Display the multiplication table for the number
print("Multiplication Table for", num)
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

"""### 3. Write a Python Program to Print the Fibonacci sequence?

"""

# Get the number of terms from the user
nterms = int(input("How many terms? "))

# Initialize the first two terms of the sequence
n1 = 0
n2 = 1

# Check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence:")
   print(n1)
else:
   print("Fibonacci sequence:")
   # Print the first two terms
   print(n1)
   print(n2)
   # Loop to generate the remaining terms
   for i in range(2, nterms):
       nth = n1 + n2
       print(nth)
       # Update the values of n1 and n2
       n1 = n2
       n2 = nth

"""### 4. Write a Python Program to Check Armstrong Number?"""

# Get the number from the user
num = int(input("Enter a number: "))

# Find the number of digits in the number
num_digits = len(str(num))

# Initialize the sum variable
sum = 0

# Calculate the sum of the cubes of the digits
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** num_digits
   temp //= 10

# Check if the number is an Armstrong number
if num == sum:
   print(num, "is an Armstrong number")
else:
   print(num, "is not an Armstrong number")

"""### 5. Write a Python Program to Find Armstrong Number in an Interval?"""

# Get the interval from the user
lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))

# Check each number in the interval
for num in range(lower, upper+1):
   # Find the number of digits in the number
   num_digits = len(str(num))
   
   # Initialize the sum variable
   sum = 0
   
   # Calculate the sum of the cubes of the digits
   temp = num
   while temp > 0:
      digit = temp % 10
      sum += digit ** num_digits
      temp //= 10
   
   # Check if the number is an Armstrong number
   if num == sum:
      print(num)

"""### 6. Write a Python Program to Find the Sum of Natural Numbers?"""

# Get the limit from the user
limit = int(input("Enter a limit: "))

# Initialize the sum variable
sum = 0

# Use a for loop to add up the natural numbers up to the limit
for num in range(1, limit + 1):
    sum += num

# Print out the sum
print("The sum of natural numbers up to", limit, "is", sum)

