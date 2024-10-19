'''
判断给定的链表中是否有环。如果有环则返回true，否则返回false。


使用 快慢指针
'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
# 
# @param head ListNode类 
# @return bool布尔型
#

class Solution:
    def hasCycle(self , head: ListNode) -> bool:
      fast = head # fast pointer
      slow = head # slow pointer
      while fast and slow and fast.next: # make sure the next is not null, otherwise return False
        fast = fast.next.next # move fast
        slow = slow.next # move slow
        # if there exists circle, fast and slow will meet "equal"
        if fast == slow and fast and slow: # check if fast meet slow 追上 表明存在循环
          return True

      return False
