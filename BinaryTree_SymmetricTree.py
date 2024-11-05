'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
      # check if the root is null
      if not root:
        return True

      # helper function for recursive
        
      def helper(node1, node2):
        
        if not node1 and not node2: # means all null -> reach end, symmetric
          return True
        elif not node1 or not node2: # means either one is NULL, not symmetric (or means one has to be NULL)
          return False
        
        # Both not NULL -> check if the val same, and recursive continue 
        return node1.val == node2.val and helper(node1.left, node2.right) and helper(node1.right, node2.left)


      return helper(root.left, root.right)
