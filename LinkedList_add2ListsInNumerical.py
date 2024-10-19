'''
假设链表中每一个节点的值都在 0 - 9 之间，那么链表整体就可以代表一个整数。
给定两个这种链表，请生成代表两个整数相加值的结果链表。

输入：
[9,3,7],[6,3]

返回值：
{1,0,0,0}

'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param head1 ListNode类 
# @param head2 ListNode类 
# @return ListNode类
#
class Solution:
    def addInList(self , head1: ListNode, head2: ListNode) -> ListNode:
      # directly add all nodes into a string for calculation
      list1 = ''
        while head1:
            list1 += str(head1.val)
            head1 = head1.next

        list2 = ''
        while head2:
            list2 += str(head2.val)
            head2 = head2.next

        res = list(str(int(list1) + int(list2)))

        new_head = ListNode(int(res[0]))
        point = new_head

        for i in range(1, len(res)):
            point.next = ListNode(int(res[i]))
            point = point.next

        return new_head
