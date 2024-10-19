'''

链表中环的入口结点
Will be similar to the Find if a list contains cycle, but to print the entry node

'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
      # First to find if the List has cycle
      # use the same fast and slow pointers
      fast = pHead
      slow = pHead

      while fast and slow and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow: # two pointers meet
          fast = pHead # reset one pointer to the head and iterate both pointer from head and from where two met
          while fast != pHead: # iterate until two pointers meet again, that will be the entry for the cycle
            fast = fast.next
            slow = slow.next

          return fast # find the entry

      return None # there is no cycle
