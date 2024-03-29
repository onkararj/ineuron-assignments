# -*- coding: utf-8 -*-
"""Programming Assignment_7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N2o8cc_Lkp7cvYbV8iTimZb2sXLxHXtc

## Programming Basic Assignment 7

### 1. Write a Python Program to find sum of array?
"""

# Function to find sum of array elements
def array_sum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

# Sample array
arr = [1, 2, 3, 4, 5]

# Calling the function
result = array_sum(arr)

# Printing the result
print("The sum of the array elements is:", result)

"""### 2. Write a Python Program to find largest element in an array?

"""

# Function to find the largest element in an array
def find_largest(arr):
    # Assume the first element is the largest
    largest = arr[0]
    # Iterate through the array to find the largest element
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest

# Sample array
arr = [3, 7, 1, 9, 5]

# Calling the function
result = find_largest(arr)

# Printing the result
print("The largest element in the array is:", result)

"""### 3. Write a Python Program for array rotation?"""

def rotate_array(arr, n):
    """Rotates an array 'arr' by 'n' positions"""
    # Calculate the number of rotations required
    n = n % len(arr)

    # Rotate the array by 'n' positions
    arr = arr[n:] + arr[:n]

    # Return the rotated array
    return arr


# Test the function with an example array
arr = [1, 2, 3, 4, 5]
n = 2
rotated_arr = rotate_array(arr, n)
print("Original Array: ", arr)
print("Rotated Array: ", rotated_arr)

"""### 4. Write a Python Program to Split the array and add the first part to the end?"""

def split_array(arr, n, k):
    # Create an empty temporary array
    temp = [0] * k

    # Store the first k elements in the temporary array
    for i in range(k):
        temp[i] = arr[i]

    # Shift the remaining elements to the left
    for i in range(k, n):
        arr[i-k] = arr[i]

    # Copy the temporary array to the end of the original array
    for i in range(k):
        arr[n-k+i] = temp[i]

    return arr

# Example usage
arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
k = 2
result = split_array(arr, n, k)
print(result)

"""### 5. Write a Python Program to check if given array is Monotonic?"""

def is_monotonic(array):
    # Determine if the array is non-increasing or non-decreasing
    non_decreasing = all(array[i] <= array[i+1] for i in range(len(array)-1))
    non_increasing = all(array[i] >= array[i+1] for i in range(len(array)-1))
    
    # Return True if either condition is met
    return non_decreasing or non_increasing

# Example usage
array1 = [1, 2, 3, 4, 5]
array2 = [5, 4, 3, 2, 1]
array3 = [1, 2, 2, 3, 4]
array4 = [4, 3, 2, 2, 1]

print(is_monotonic(array1))  
print(is_monotonic(array2))  
print(is_monotonic(array3))  
print(is_monotonic(array4))

