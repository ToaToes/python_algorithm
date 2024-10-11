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
str[5:]: This will return the string starting from the sixth character to the end. </br>
str[1:5]: This will return the characters from index 1 to index 4 (not including index 5). </br>

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


