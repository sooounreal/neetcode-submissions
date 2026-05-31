# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid using two pointers
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        
        mid = prev if not fast else slow
        # reverse second half
        prev = None
        cur = mid
        next_ = cur.next
        while next_:
            cur.next = prev
            prev = cur
            cur = next_
            next_ = next_.next
        cur.next = prev
        # cur is now at tail

        right = cur
        left = head
        # join two halves
        while left and right:
            l_next = left.next
            left.next = right
            r_next = right.next
            right.next = l_next
            left = l_next
            right = r_next
        
        
