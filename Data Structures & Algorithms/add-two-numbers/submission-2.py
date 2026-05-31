# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        cur1 = l1
        cur2 = l2

        cur = ListNode()
        start = cur
        carry = 0
        while cur1 or cur2:
            val1 = cur1.val if cur1 else 0
            val2 = cur2.val if cur2 else 0
            s = val1 + val2 + carry
            if s >= 10:
                single = ListNode(s%10)
                carry = 1
                cur.next = single
            else:
                cur.next = ListNode(s)
                carry = 0
            cur = cur.next
            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
        if carry != 0:
            cur.next = ListNode(carry)
        return start.next
