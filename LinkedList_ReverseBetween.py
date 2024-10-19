'''
描述
将一个节点数为 size 链表 m 位置到 n 位置之间的区间反转，要求时间复杂度 O(n)，空间复杂度 O(1)。

例如：
给出的链表为 1→2→3→4→5→NULL, m=2,n=4,

返回 1→4→3→2→5→NULL.

数据范围： 链表长度 0<size≤1000，0<m≤n≤size，链表中每个节点的值满足 ∣val∣≤1000

要求：时间复杂度 O(n) ，空间复杂度 O(n)
进阶：时间复杂度 O(n)，空间复杂度 O(1)
'''


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # Create a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        
        # Step 1: Move `pre` to the node just before the reversal starts
        for _ in range(m - 1):
            pre = pre.next
            
        # Step 2: Reverse the nodes from m to n
        cur = pre.next  # The first node to reverse
        for _ in range(n - m):
            temp = cur.next  # The node to be moved
            cur.next = temp.next  # Remove `temp` from the current position
            temp.next = pre.next  # Insert `temp` right after `pre`
            pre.next = temp  # Update the `pre` pointer
        
        # Return the new head of the list
        return dummy.next
