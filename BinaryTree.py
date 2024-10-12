'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.

'''
'''
In-Order Traversal
Post-Order Traversal
Pre-Order Traversal

'''
# In-Order:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        dynamic_arr = []

        def recursive(root):
            if not root:
                return []

            recursive(root.left)
            dynamic_arr.append(root.val)
            recursive(root.right)

        recursive(root)

        return dynamic_arr
