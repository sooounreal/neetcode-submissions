# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        cur = head
        heap = []

        for i in range(len(lists)):
            if lists[i] is None:
                continue
            heapq.heappush(heap, (lists[i].val, i))
        while heap:
            val, i = heapq.heappop(heap)
            cur.next = lists[i]
            cur = lists[i]
            lists[i] = lists[i].next
            if lists[i] is not None:
                heapq.heappush(heap, (lists[i].val, i))
        return head.next
        

            
