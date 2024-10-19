'''
链表中倒数最后k个结点
'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pHead ListNode类 
# @param k int整型 
# @return ListNode类
#
class Solution:
    def FindKthToTail(self , pHead: ListNode, k: int) -> ListNode:
      # write code here
      # Fist check if k exceeds the length of the list
      count = 0
      check = pHead
      while check:
        check = check.next
        count += 1

      if k > count:
        return None

      for _ in range(count - k): # iterate until the last Kth element, then return
        pHead = pHead.next

      return pHead # the Kth element
          
