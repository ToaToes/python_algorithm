'''
合并 k 个升序的链表并将结果作为一个升序的链表返回其头节点。

Wrapper 类: 这是一个包装类，帮助我们在最小堆中比较 ListNode 对象。它重载了 < 运算符，以便根据节点的值进行比较。

最小堆: 使用 Python 的 heapq 模块创建一个最小堆，将所有链表的头节点放入堆中。

合并链表:

通过不断从堆中取出最小的节点，并将其链接到结果链表中。
如果取出的节点还有后续节点，就将其后续节点放入堆中。
返回结果: 最后，返回虚拟头节点的下一个节点，即合并后的链表头节点。

时间复杂度合并 k 个链表的时间复杂度为 O(Nlogk)，其中 N 是所有链表节点的总数，因为每次插入和删除堆的操作都是 O(logk)。
这种方法效率高且易于理解，适用于合并多个有序链表的情况。
'''

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        # 定义一个比较函数，以便在堆中使用 ListNode 对象
        class Wrapper:
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val
        
        # 创建一个最小堆
        min_heap = []
        
        # 将所有链表的头节点加入堆中
        for l in lists:
            if l:
                heapq.heappush(min_heap, Wrapper(l))
        
        # 创建一个虚拟头节点，以便简化链表操作
        dummy = ListNode(0)
        current = dummy
        
        # 当堆不为空时，不断从堆中取出最小的节点
        while min_heap:
            # 取出最小节点
            smallest_node = heapq.heappop(min_heap).node
            current.next = smallest_node
            current = current.next
            
            # 如果该节点还有后续节点，放入堆中
            if smallest_node.next:
                heapq.heappush(min_heap, Wrapper(smallest_node.next))
        
        # 返回合并后的链表头节点
        return dummy.next


