'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
'''

# To well know Single Link List Node Data structure usage


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # To eliminate [],[] and [][1,2,3] and [1,2,3][] cases
        if not list1 and not list2:
            return list1
        elif not list1:
            return list2
        elif not list2:
            return list1

        #create a head and a pointer
        current = res = ListNode()

        # To compare both nodes at the same time and push to the next node
        while list1 and list2:
            if list1.val >= list2.val:
                current.next = list2
                current = current.next
                list2 = list2.next
            else:
                current.next = list1
                current = current.next
                list1 = list1.next

        # When one list reach null node, just point next to the other list
        if not list1:
            current.next = list2
        elif not list2:
            current.next = list1

        # return the head created
        return res.next

'''
current = res = ListNode()
both current and res point to the same new create node

a = b = 1
a += 2
print(b)
b = 2
'''

            




