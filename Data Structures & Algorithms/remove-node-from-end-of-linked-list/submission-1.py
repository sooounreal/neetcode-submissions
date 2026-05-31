# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        cur = head
        size = 1
        while cur.next:
            cur = cur.next
            size += 1

        dummy = ListNode()
        dummy.next = head
        cur = dummy
        for _ in range(size-n):
            cur = cur.next

        if cur.next:
            cur.next = cur.next.next
        # 1 -> 2 -> 3 -> 4, size = 4, n = 2, del 3
        # dummy -> head
        return dummy.next
