'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.


Input: head = [1,1,2]
Output: [1,2]

Input: head = [1,1,2,3,3]
Output: [1,2,3]

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
      current = ListNode()
      current = head
      while current and current.next:
        if current.val == current.next.val: # if find same val, move to the next next
          current.next = current.next.next
        else:
          current = current.next # iterate current pointer thougth rest linkedlist

        # return the head of the non-duplicate linked list
        return head
