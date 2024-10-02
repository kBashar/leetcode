# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappush, heappop

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        ListNode.__lt__ = lambda self, other: self.val < other.val

        for node in lists:
            if node:
                heappush(heap, node)
        
        head = ListNode(0)
        curr = head

        while len(heap) > 0 :
            node = heappop(heap)
            
            curr.next = node
            curr = node

            if node.next:
                heappush(heap, node.next)
        
        return head.next
            

        



        