'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true
'''

''' 
Solve problem by using Stack, where matches will be pop first since its open-close in correct order,

([)]
(){}}{[]
...
will be considered as invalid
'''

class Solution:
    def isValid(self, s: str) -> bool: 
      # First to create a stack by using dequeue
      stack = dequeue()

      # set dictionary for matching (){}[]
      translation = {
        "{": "}",
        "(": ")",
        "[": "]",
      }

      # iterate through string
      for char in s:
        # put opens in stack, follow FILO order (by correct open close order)
        if(char == '(' or char == '{' or char == '['):
          stack.append(char)
        # match for close in stack by checking pop order
        elif(char == ')' or char == '}' or char == ']'):
          # check if stack is already empty, empty means more closes than opens
          if not stack:
            return False
          # check if close matches pop open , by translation
          elif (char != translation[stack.pop()]):
            return False

      # check if after pop, stack empty
      if not stack:
        return True
      # if stack not empty, meaning there are more opens than closes
      else
        return False
    
          


