# python_algorithm
learn python basics and to solve leetcode

## 1. mapping in python:
```
translation = {

  "abc": 1,
  "sdf": 2,
  "ert": 3,

  ...
}

num = translation["abc"]
```
_____
```
# Create a translation table for characters
translation_table = str.maketrans("abc", "123")

# Translate a string using the table
original_string = "abcde"
translated_string = original_string.translate(translation_table)

print(translated_string)  # Output: "123de"

```

## 2. How to slice a string
str[:5]: This will return the first five characters. </br>
[0], [1], [2], [3], [4] </br>
str[5:]: This will return the string starting from the sixth character to the end. </br>
str[1:5]: This will return the characters from index 1 to index 4 (not including index 5). </br>

**Its always including the left, excluding the right**

arr[-1] is a way to access the last element of a list (or any sequence, such as a string or tuple). </br>
The negative indexing allows you to count from the end of the list, where -1 represents the last item, -2 represents the second-to-last item

______

## 3. How to use STACK and HEAP -> Stack(**Last In, First Out**), Heap(min-binary tree, smallest out)

In Python, a stack can be implemented using a list or the collections.deque class, which provides an efficient way to append and pop items from either end. 

**STACK: **
A stack follows the Last In, First Out (LIFO) principle, meaning the last item added is the first one removed. use the append() method to push an item onto the stack and the pop() method to remove the top item.
```
# Creating a stack using a list
stack = []

# Pushing items onto the stack
stack.append(1)
stack.append(2)
stack.append(3)

print("Stack after pushing:", stack)  # Output: [1, 2, 3]

# Popping an item from the stack
top_item = stack.pop()
print("Popped item:", top_item)       # Output: 3
print("Stack after popping:", stack)   # Output: [1, 2]

```

**Using ```collections.deque```**

more efficient for stack operations because it provides O(1) time complexity for appends and pops from either end.
```
from collections import deque

# Creating a stack using deque
stack = deque()

# Pushing items onto the stack
stack.append(1)
stack.append(2)
stack.append(3)

print("Stack after pushing:", list(stack))  # Output: [1, 2, 3]

# Popping an item from the stack
top_item = stack.pop()
print("Popped item:", top_item)              # Output: 3
print("Stack after popping:", list(stack))    # Output: [1, 2]

# Insert an element at a specific index (e.g., index 1)
stack.insert(1, 4)
print("Stack after insert:", stack)  # Output: [1, 4, 2]

# Delete an element by its index (e.g., index 0)
del stack[0]
print("Stack after delete:", stack)  # Output: [4, 2]

```


**Heap:**

import heapq

heapq.heappush() -> push into the data structure, small will keep in the root, then bigger number
heapq.heappop() -> pop the root of the tree, re-orgnize the tree and find another smallest for the root

[5, 1, 8, 2, 4, 6, 7] 

       1
      / \
     2   6
    / \ / \
   5  4 8  7

smallest will be at the root of the binary tree -> min-binary tree

_____

## 4. To use a Hash to eliminate the duplicates

In Python, when you use a dictionary (hash = {}), it functions as a hash table where keys are unique. Each key can only appear once in the dictionary. If you try to add a duplicate key, the new value will overwrite the existing one.

```
hash_table = {}

for i in nums:
  hash_table[i] = i
//OR
# Adding unique elements
hash_table['apple'] = 5
hash_table['banana'] = 2

# Attempting to add a duplicate key
hash_table['apple'] = 10  # This will update the value for 'apple'

print(hash_table)  # Output: {'apple': 10, 'banana': 2}
```
To store counts of items
```
# List of items
items = ['apple', 'banana', 'orange', 'banana']

# Dictionary to store counts
hashlist = {}

for item in items:
    if item in hashlist:
        hashlist[item] += 1  # Increment count if item exists
    else:
        hashlist[item] = 1    # Initialize count for new item

print(hashlist)  # Output: {'apple': 1, 'banana': 2, 'orange': 1}

```

```
# List with potential duplicates
items = ['apple', 'banana', 'orange', 'banana']

# Using a set for unique items
hashlist = set(items)

print(hashlist)  # Output: {'apple', 'banana', 'orange'}

```

To delete or get the value:
```
del my_hashmap['banana']  # Remove key 'banana'

# Alternatively, using pop() to remove and return the value
orange_count = my_hashmap.pop('orange')  # Removes 'orange' and returns its value

```

______

## 5. To clear sides white space and split strings into arrays

1. Strip trailing whitespaces from the input string using the strip() method.
2. Split the string into words using the split() method.
3. If there are no words after stripping whitespaces, return 0.
4. Otherwise, return the length of the last word, which is the last element in the list of words.

**s.strip():**

The strip() method removes any leading and trailing whitespace characters from the string s. This includes spaces, tabs, and newline characters.
For example, if s is " Hello World! ", then s.strip() will return "Hello World!".

**split():**

The split() method splits the string into a list of words based on whitespace by default (spaces, tabs, etc.).
If the string is "Hello World!", then split() will return ['Hello', 'World!'].
If there are multiple spaces between words, split() automatically handles them by treating consecutive whitespace as a single delimiter.

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substringconsisting of non-space characters only.
```
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()

        if not words: #the list is empty, return 0
            return 0

        print(len(words[-1]))
```
Dumb way:
```
class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # trace with two pivots
        left = right = len(s)-1
        while left >= 0:
            if s[right] == ' ':
                right -= 1
                left = right
            else:
                if s[left] != ' ':
                    left -= 1
                else:
                    return right - left

                #when left pivot reach the very begining of the s, done
                if left == -1:
                    return right - left
```


____
## 6. Splitting an Integer into Digits

```
#Define an integer
number = 12345

#Convert the integer to a string and split into digits
digits = [int(digit) for digit in str(number)]

print("Digits:", digits)  # Output: Digits: [1, 2, 3, 4, 5]

```
**Example for use:** 

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
```
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        temp = 0
        for i in range(len(digits)):
            temp += digits[i] * (10**(len(digits)-1-i)) # remeber to iterate the digits by -1 !
        
        temp += 1

        res = [int(i) for i in str(temp)]

        return res
```

______

## 7. To check a length of an Integer: first covert to string

```
# Define an integer
number = 12345

# Convert to string and use len()
length = len(str(number))

print("Number of digits:", length)  # Output: Number of digits: 5

```

_____

## 8. Conversion between Binary AND Integer

```
# Convert Int to Binary
# Define a binary string
binary_string = '1011'

# Convert binary string to integer
integer_value = int(binary_string, 2)

print("The integer value of binary", binary_string, "is:", integer_value)  # Output: 11



# Convert Binary to Int
# Define an integer
number = 11

# Convert the integer to binary
binary_string = bin(number)

print("The binary representation of", number, "is:", binary_string)  # Output: 0b1011

# To remove the 0b in the front
res = str(number)[2:] # slice the "str" array from 2 to the rest

```
Example for usage:
```
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


class Solution:
    def addBinary(self, a: str, b: str) -> str:

        int_c = int(str(a), 2) + int(str(b), 2)

        bin_c = bin(int_c)

        res = str(bin_c)[2:]

        return res
```

______
## 9. DP Table

A DP table (Dynamic Programming table) in Python is a data structure used to store intermediate results of subproblems in dynamic programming algorithms. This approach helps to avoid redundant calculations by storing results of subproblems, allowing for efficient computation of larger problems.

Key Concepts
Dynamic Programming: It’s an optimization technique used to solve complex problems by breaking them down into simpler overlapping subproblems. The results of these subproblems are stored (usually in a table) so they can be reused.

DP Table: Typically a 2D list (or array) in Python, where:

Rows represent one dimension of the problem.
Columns represent another dimension of the problem.


_____
## 10. Array in python: assign and copy

To reference the same location: modify any arr will make change on another arr
```
arr1 = [1, 2, 3]
arr2 = [2, 3, 4]

arr1 = arr2  # arr1 now references the same list as arr2

# Modifying arr1
arr1.append(5)

print(arr1)  # Output: [2, 3, 4, 5]
print(arr2)  # Output: [2, 3, 4, 5]  (also modified)

```

Not to reference to the same memo location
```
arr1 = arr2.copy()  # Creates a shallow copy of arr2

# Modifying arr1
arr1.append(5)

print(arr1)  # Output: [2, 3, 4, 5]
print(arr2)  # Output: [2, 3, 4]  (not modified)

```

**NOTE!!! Also copy() and deepcopy() and a[:]**
1. ```copy()```
This method creates a shallow copy of the object. <br/>
means that it creates a new object, but it inserts references to the original objects contained in the original. <br/>
If the original object contains nested objects (like lists or dictionaries), the references to those nested objects are copied, not the nested objects themselves. <br/>
Changes to mutable nested objects in the original will reflect in the shallow copy. <br/>
```
import copy

original = [1, 2, [3, 4]]
shallow_copy = copy.copy(original)

original[2][0] = 'changed'
print(shallow_copy)  # Output: [1, 2, ['changed', 4]]

```
2. ```deepcopy()```
This method creates a deep copy of the object, means that it creates a new object and recursively copies all objects found within the original, <br/>
meaning that all nested objects are also copied. Changes to any nested objects in the original do not affect the deep copy. <br/>
```
import copy

original = [1, 2, [3, 4]]
deep_copy = copy.deepcopy(original)

original[2][0] = 'changed'
print(deep_copy)  # Output: [1, 2, [3, 4]]

```

3. ```a[:]``` its the same as ```copy()```

**TO Assign number in array by 2**
```
arr[0, 1, 2, 3, 4, 5, 6]

arr[::2] -> 0, 2, 4, 6: from 0 step 2

arr[1::2] -> 1, 3, 5: from 1 step 2
```

**To remove one element in array**
```
# Initialize a list
my_list = [1, 2, 3, 2, 4]

# Remove the first occurrence of 2
my_list.remove(2)

print(my_list)  # Output: [1, 3, 2, 4]

```
**To add one element in array**
```
# Initialize an empty list
my_list = []

# Append elements to the list
my_list.append(1)
my_list.append(2)
my_list.append(3)

print(my_list)  # Output: [1, 2, 3]

```

**TO Adds all elements from an iterable (like another list) to the end of the list.**
```
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  # Output: [1, 2, 3, 4, 5]

```

**To insert an element at specific index**
```
my_list = [1, 2, 3]
my_list.insert(1, 4)  # Insert 4 at index 1
print(my_list)  # Output: [1, 4, 2, 3]

```

**To remove and also return the element at specific index**
```
my_list = [1, 2, 3]
popped_element = my_list.pop()
print(popped_element)  # Output: 3
print(my_list)         # Output: [1, 2]

```

**TO get the number of specific element from one array**
```
my_list = [1, 2, 3, 2]
count_of_two = my_list.count(2)
print(count_of_two)  # Output: 2

```

**Remove all elements from the List**
```
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Output: []
```

_____

## 11. To Sort ——> sorted(arr) & arr.sort()

**arr.sort()**
```
arr = [3, 1, 4, 2]
arr.sort(reverse=True)  # Sorts in place in descending order
print(arr)  # Output: [4, 3, 2, 1]

```

**sorted(arr)**
```
arr = [3, 1, 4, 2]
arr = sorted(arr)  # arr now refers to the new sorted list

print(arr)        # Output: [1, 2, 3, 4]

___________________________________________________________
original = [3, 1, 4, 2]
arr = sorted(original)

print(original)  # Output: [3, 1, 4, 2] (unchanged)
print(arr)       # Output: [1, 2, 3, 4] (new sorted list)
```

2D array sorted base on certain element ->
```
list = sorted(array, key = lambda x: x[1]) # sort base on second element in 2d

# class Interval:
#     def __init__(self, a=0, b=0):
#         self.start = a
#         self.end = b

list = sorted(interval, key = lambda x: x.start) # sort base on x.start item
```

**Sort a list of tuples (or other iterable items) based on multiple criteria. **

```
sorted(array, key = lambda x: (-x[0], x[1])) -> 倒叙第一位排序， 如果相同就正序排第二位
sorted(array, key = lambda x: (x[0], x[1])) -> 正序第一位排序， 如果相同就正序排第二位

```
will first be based on the first element of the tuple (or list), and if there are ties (i.e., multiple elements have the same first element), it will then sort by the second element.

## 11. Helper methods in dealing with **STRING**

```
text = "hello world"
upper_text = text.upper()
print(upper_text)  # Output: "HELLO WORLD"

```
```
text = "HELLO WORLD"
lower_text = text.lower()
print(lower_text)  # Output: "hello world"

```
```
text = "hello world"
capitalized_text = text.capitalize()
print(capitalized_text)  # Output: "Hello world"

```
```
text = "hello world"
title_text = text.title()
print(title_text)  # Output: "Hello World"

```
```
text = "Hello World"
swapped_text = text.swapcase()
print(swapped_text)  # Output: "hELLO wORLD"

```
```
# Sample string
text = "Hello world, this is a test."

# Splitting the string into a list of words
words = text.split()

# Output the result
print(words)  # Output: ['Hello', 'world,', 'this', 'is', 'a', 'test.']

_______

# Using a comma as the delimiter
text = "apple,banana,cherry"
fruits = text.split(',')
print(fruits)  # Output: ['apple', 'banana', 'cherry']

_____

import re

text = "Hello world, this is a test!"
# Splitting and removing punctuation
words = re.findall(r'\b\w+\b', text)
print(words)  # Output: ['Hello', 'world', 'this', 'is', 'a', 'test']

```

```
# Original string
text = "Hello world, this is a test."

# Split the string into a list of words
words = text.split()

# Reconstruct the string from the list of words
reconstructed = ' '.join(words)

# Output the result
print(reconstructed)  # Output: "Hello world, this is a test."

_______

# Using a comma as a separator
reconstructed_with_commas = ', '.join(words)
print(reconstructed_with_commas)  # Output: "Hello, world,, this, is, a, test."

```

________

## 12. Check if a number is Hexdecimal/others

```
def is_hexadecimal(strs):
  try:
    int(strs, 16)
    return True
  except ValueError:
    return False
```

________

## 13. Floor and Ceiling of a number

In Python, you can use the math module to apply the floor function, which rounds down a number to the nearest integer. Here's how to do it:

use math.floor()
```
import math

number = 3.7
floored_value = math.floor(number)
print(floored_value)  # Output: 3

```
OR use ```n//2```


use int()
```
number = 3.7
floored_value = int(number)
print(floored_value)  # Output: 3

```
