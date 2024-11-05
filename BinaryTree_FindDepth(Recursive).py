'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


IMPORTANT: 
To set ma and temp as global variables in Python and modify them within your helper function, you would need to use the global keyword. 
This tells Python that the variables ma and temp are not local to the helper function, but rather global to the entire script (or module).

However, using global variables in this context can lead to some undesired complexity and make the code harder to maintain.
That’s why the recursive approach I suggested earlier avoids using global variables. Nevertheless, 
if you're specifically asking how to use them, here's an example of how you would modify the code to use global variables:


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        global ma, temp  -> To set global var
        ma = 0
        temp = 0
        
        def helper(root):
            global ma, temp
            if not root:
                # Update ma with the maximum of current temp and existing ma
                ma = max(temp, ma)
                temp = 0  # Reset temp
            else:
                temp += 1
                helper(root.left)  # Traverse left subtree
                helper(root.right)  # Traverse right subtree
        
        helper(root)
        return ma

SO normally do not use global variables
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
      if not root: # NULL -> 0 height
        return 0

      def helper(root): # recursive to measure
        if not root: # reach NULL -> reach edge, get 0
          return 0
        else: # not NULL, add 1 to the height and continue to find left and right node
          return 1 + max(helper(root.left), helper(root.right)) # find max of right nodetree or left nodetree

      return helper(root)
