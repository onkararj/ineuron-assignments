# -*- coding: utf-8 -*-
"""Programming Assignment_12.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UgM_zWkqJfkbMx02eNKBD665tod5t8O8

# Python Basic Programming Assignment 12
-------------

### 1. Write a Python program to Extract Unique values dictionary values?
"""

# Sample dictionary
my_dict = {'a': [1, 2, 3], 'b': [2, 3, 4], 'c': [3, 4, 5], 'd': [4, 5, 6]}

# Initialize an empty set to store the unique values
unique_values = set()

# Loop through the dictionary values and add each value to the set
for values in my_dict.values():
    unique_values.update(values)

# Convert the set to a list to get the unique values
unique_values_list = list(unique_values)

# Print the unique values
print(unique_values_list)

"""### 2. Write a Python program to find the sum of all items in a dictionary?"""

my_dict = {'a': 10, 'b': 20, 'c': 30}

sum_values = 0

for value in my_dict.values():
    sum_values += value

print(f"The sum of all items in the dictionary is {sum_values}")

"""### 3. Write a Python program to Merging two Dictionaries?"""

dict1 = {'a': 10, 'b': 20}
dict2 = {'c': 30, 'd': 40}

dict1.update(dict2)

print(dict1)

"""### 4. Write a Python program to convert key-values list to flat dictionary?"""

key_value_list = [("a", 1), ("b", 2), ("c", 3), ("d", 4)]

flat_dict = {}

for key, value in key_value_list:
    flat_dict[key] = value

print(flat_dict)

"""### 5. Write a Python program to insertion at the beginning in OrderedDict?"""

from collections import OrderedDict

# Create an empty ordered dictionary
od = OrderedDict()

# Insert some elements at the end of the ordered dictionary
od['one'] = 1
od['two'] = 2
od['three'] = 3

# Print the ordered dictionary
print("Before insertion:")
print(od)

# Move the last element to the beginning of the ordered dictionary
od.move_to_end('three', last=False)

# Add a new element at the beginning of the ordered dictionary
od.update({'zero': 0})

# Print the ordered dictionary after insertion
print("After insertion:")
print(od)

"""### 6. Write a Python program to check order of character in string using OrderedDict()?"""

from collections import OrderedDict

def check_char_order(string, pattern):
    # Create an ordered dictionary to store the index of each character in the pattern
    pattern_dict = OrderedDict((char, idx) for idx, char in enumerate(pattern))

    # Initialize the index to -1
    prev_index = -1

    # Loop through the characters in the string
    for char in string:
        # If the current character is in the pattern dictionary
        if char in pattern_dict:
            # Get the index of the character in the pattern dictionary
            curr_index = pattern_dict[char]

            # If the current index is less than the previous index, the order is incorrect
            if curr_index < prev_index:
                return False

            # Update the previous index to the current index
            prev_index = curr_index

    # If we get to this point, the order is correct
    return True

# Example usage
string = "hello world"
pattern = "hlo"
if check_char_order(string, pattern):
    print(f"The characters in '{pattern}' appear in order in '{string}'")
else:
    print(f"The characters in '{pattern}' do not appear in order in '{string}'")

"""### 7. Write a Python program to sort Python Dictionaries by Key or Value?"""

# dictionary to be sorted
d = {'apple': 2, 'banana': 1, 'orange': 3}

# sort by key
sorted_dict_by_key = dict(sorted(d.items()))

# sort by value
sorted_dict_by_value = dict(sorted(d.items(), key=lambda item: item[1]))

print("Sorted by key:", sorted_dict_by_key)
print("Sorted by value:", sorted_dict_by_value)

