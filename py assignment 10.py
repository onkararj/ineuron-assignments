# -*- coding: utf-8 -*-
"""Programming Assignment_10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sy86HegaTdJnDZr6TgtRKT7FPTkOborg

## Python Basic Programming Assignment 10

### 1. Write a Python program to find sum of elements in list?
"""

def sum_list(lst):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list and add up each element
    for num in lst:
        total += num

    return total

# Example usage:
my_list = [1, 2, 3, 4, 5]
list_sum = sum_list(my_list)
print(list_sum)

"""### 2. Write a Python program to  Multiply all numbers in the list?"""

def multiply_list(lst):
    # Initialize a variable to store the product
    product = 1

    # Loop through the list and multiply each element
    for num in lst:
        product *= num

    return product

# Example usage:
my_list = [1, 2, 3, 4, 5]
list_product = multiply_list(my_list)
print(list_product)

"""### 3. Write a Python program to find smallest number in a list?"""

def find_smallest(lst):
    # Assume the first element is the smallest
    smallest = lst[0]

    # Loop through the list and compare each element to the current smallest
    for num in lst:
        if num < smallest:
            smallest = num

    return smallest

# Example usage:
my_list = [3, 5, 2, 8, 1]
smallest_num = find_smallest(my_list)
print(smallest_num)

"""### 4. Write a Python program to find largest number in a list?"""

def find_largest(lst):
    # Assume the first element is the largest
    largest = lst[0]

    # Loop through the list and compare each element to the current largest
    for num in lst:
        if num > largest:
            largest = num

    return largest

# Example usage:
my_list = [3, 5, 2, 8, 1]
largest_num = find_largest(my_list)
print(largest_num)

"""### 5. Write a Python program to find second largest number in a list?"""

def find_second_largest(lst):
    # Assume the first element is the largest and the second largest
    largest = lst[0]
    second_largest = lst[1] if lst[1] < largest else lst[0]

    # Loop through the list and update the largest and second largest variables as needed
    for num in lst[1:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest

# Example usage:
my_list = [3, 5, 2, 8, 1]
second_largest_num = find_second_largest(my_list)
print(second_largest_num)

"""### 6. Write a Python program to find N largest elements from a list?"""

def find_n_largest(lst, n):
    # Sort the list in descending order
    sorted_lst = sorted(lst, reverse=True)

    # Return the first N elements of the sorted list
    return sorted_lst[:n]

# Example usage:
my_list = [3, 5, 2, 8, 1]
n_largest_nums = find_n_largest(my_list, 2)
print(n_largest_nums)

"""### 7. Write a Python program to print even numbers in a list?"""

def print_even_numbers(lst):
    # Loop through each element in the list
    for num in lst:
        # Check if the element is even
        if num % 2 == 0:
            print(num)

# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_even_numbers(my_list)

"""### 8. Write a Python program to print odd numbers in a List?"""

def print_odd_numbers(lst):
    # Loop through each element in the list
    for num in lst:
        # Check if the element is odd
        if num % 2 != 0:
            print(num)

# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_odd_numbers(my_list)

"""### 9. Write a Python program to Remove empty List from List?"""

def remove_empty_lists(lst):
    # Use a list comprehension to create a new list with non-empty lists
    return [sublst for sublst in lst if sublst]

# Example usage:
my_list = [[1, 2], [], [3, 4, 5], [], [6]]
new_list = remove_empty_lists(my_list)
print(new_list)

"""### 10. Write a Python program to Cloning or Copying a list?"""

original_list = [1, 2, 3, 4, 5]

# Using the copy() method to clone the list
new_list = original_list.copy()

# Or using the list() constructor to create a copy
new_list = list(original_list)

# Or using slicing to create a copy
new_list = original_list[:]

# Testing the result
print(original_list) 
print(new_list)

"""### 11. Write a Python program to Count occurrences of an element in a list?"""

def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

# Example usage
my_list = [1, 2, 3, 4, 4, 4, 5]
num_occurrences = count_occurrences(my_list, 4)
print(f"The number of occurrences of 4 in the list is {num_occurrences}.")

