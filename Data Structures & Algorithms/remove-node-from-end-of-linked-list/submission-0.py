# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        cur = head
        total_len = 0
        while cur:
            total_len += 1
            cur = cur.next
        
        m = total_len - n
        if m == 0:
            return head.next
        prev = None
        cur = head
        next_ = head.next
        for i in range(m):
            prev = cur
            cur = next_
            next_ = next_.next
   
        prev.next = next_
        return head
        