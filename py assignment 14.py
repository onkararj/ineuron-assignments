# -*- coding: utf-8 -*-
"""Programming Assignment_14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pRWgLOx_yLPJkkCAssuA8O5i6F1XGLSh

## Python Basic Programming Assignment - 14
---------------------

### 1. Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
"""

class DivisibleBySeven:
    def __init__(self, n):
        self.n = n

    def divisible_by_seven(self):
        for i in range(self.n):
            if i % 7 == 0:
                yield i
# create an instance of the class with n = 50
divisible_by_seven = DivisibleBySeven(50)

# use the generator to iterate over the numbers that are divisible by 7
for num in divisible_by_seven.divisible_by_seven():
    print(num)

"""
### 2. Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically."""

from collections import Counter

# Input string
input_str = "Hello world! This is a onkar arjunwade."

# Convert input string to list of words
words_list = input_str.split()

# Count frequency of each word
word_freq = Counter(words_list)

# Sort words alphabetically
sorted_words = sorted(word_freq.keys())

# Print frequency of each word
for word in sorted_words:
    print(f"{word}: {word_freq[word]}")

"""
### 3. Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class."""

class Person:
    def getGender(self):
        pass

class Male(Person):
    def getGender(self):
        print("Male")

class Female(Person):
    def getGender(self):
        print("Female")

person1 = Male()
person2 = Female()

person1.getGender() 
person2.getGender()

"""
### 4. Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ['Play', "Love"] and the object is in ["Hockey","Football"]."""

subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey", "Football"]

for subject in subjects:
    for verb in verbs:
        for obj in objects:
            sentence = subject + " " + verb + " " + obj
            print(sentence)

"""
### 5. Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!"
"""

import gzip

string = "hello world!hello world!hello world!hello world!"

# Compress the string
compressed_data = gzip.compress(string.encode('utf-8'))

# Decompress the string
decompressed_data = gzip.decompress(compressed_data).decode('utf-8')

print("Original string:", string)
print("Compressed data:", compressed_data)
print("Decompressed string:", decompressed_data)

"""
### 6. Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list."""

def binary_search(arr, x):
    
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == x:
            return mid
        
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    
    # If the element is not found, return -1
    return -1
arr = [1, 2, 4, 5, 6, 7, 8, 9]
x = 5

result = binary_search(arr, x)
print(result)

