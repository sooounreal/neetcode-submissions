# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # find number of nodes, do k%n
        # link last to head - creates cycle
        # unlink new tail to head
        # move head -> n-k%n
        if not head:
            return head

        cur = head
        n = 1
        while cur.next:
            cur = cur.next
            n += 1
        
        # link tail to head
        cur.next = head

        k = k % n
        # move head
        cur = head
        for i in range(n-k-1):
            cur = cur.next
        
        res = cur.next
        cur.next = None
        return res