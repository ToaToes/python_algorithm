# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
      # To compare cases like [] [] and [] [0]
      if not q and not p:
        return True
      elif not q or not p:
        return False
      
      # use recursive to go through tree
      def checkTree(p, q):
        # if both NULL case, means the same nodes 
        if not p and not q:
          return True

        # check right and left if they are not NULL and have same val
        if p and q and p.val = q.val:
          return checkTree(p.left, q.left) and checkTree(p.right, q.right)

        # return False if non met
        return False

      return checkTree(p, q)
