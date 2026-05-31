# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev = None
        cur = head
        next_ = cur.next

        while next_:
            cur.next = prev
            prev = cur
            cur = next_
            next_ = next_.next
 
        cur.next = prev
        return cur
