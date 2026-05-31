# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur1 = head
        cur2 = head.next

        while cur1 and cur2 and cur1.next and cur2.next:
            if cur1 == cur2:
                return True
            cur1 = cur1.next
            cur2 = cur2.next.next

        return False