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

## 3. How to use STACK

In Python, a stack can be implemented using a list or the collections.deque class, which provides an efficient way to append and pop items from either end. 

**Using a List**
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

```

_____

# To use a Hash to eliminate the duplicates

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

# To clear sides white space and split strings into arrays

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

                if left == -1:
                    return right - left
```
