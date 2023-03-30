# -*- coding: utf-8 -*-
"""Programming Assignment_8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jxxXt22fiDT_Df-ByRZ-I4DHYdys-dQH

# Python Basic Programming Assignment 8

### 1. Write a Python Program to Add Two Matrices?
"""

# Define two matrices
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[10, 11, 12],
           [13, 14, 15],
           [16, 17, 18]]

# Create a result matrix with the same dimensions as the input matrices
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# Iterate over each element of the matrices and add them
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

# Print the result matrix
print("The sum of the two matrices is:")
for row in result:
    print(row)

"""### 2. Write a Python Program to Multiply Two Matrices?"""

# Function to multiply two matrices
def matrix_multiplication(matrix1, matrix2):
    # Check if matrices can be multiplied
    if len(matrix1[0]) != len(matrix2):
        return "Matrices cannot be multiplied"
    
    # Initialize the resulting matrix with zeros
    result_matrix = [[0 for j in range(len(matrix2[0]))] for i in range(len(matrix1))]
    
    # Multiply the matrices
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result_matrix


# Test the function
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result_matrix = matrix_multiplication(matrix1, matrix2)
print(result_matrix)

"""### 3. Write a Python Program to Transpose a Matrix?"""

# take the input of the matrix from the user
matrix = []
r = int(input("Enter the number of rows: "))
c = int(input("Enter the number of columns: "))
for i in range(r):
    row = []
    for j in range(c):
        num = int(input(f"Enter the element at [{i}][{j}]: "))
        row.append(num)
    matrix.append(row)

# print the original matrix
print("Original Matrix:")
for row in matrix:
    print(row)

# transpose the matrix
transpose = []
for j in range(c):
    row = []
    for i in range(r):
        row.append(matrix[i][j])
    transpose.append(row)

# print the transposed matrix
print("Transposed Matrix:")
for row in transpose:
    print(row)

"""
### 4. Write a Python Program to Sort Words in Alphabetic Order?
"""

# Get input from user
words = input("Enter words separated by space: ")

# Split words into a list
words_list = words.split()

# Sort the list in alphabetical order
words_list.sort()

# Print the sorted list
print("Sorted words: ")
for word in words_list:
    print(word)

"""### 5. Write a Python Program to Remove Punctuation From a String?"""

import string

def remove_punctuation(input_string):
   
    # create a set of all punctuation marks
    punctuation = set(string.punctuation)
    # remove punctuation marks from the string
    no_punct = ''.join(char for char in input_string if char not in punctuation)
    return no_punct

# Example usage
input_string = "Hello, World! This is a Python program."
output_string = remove_punctuation(input_string)
print(output_string)
# Output: Hello World This is a Python program

