# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        carry = 0

        cur = res
        cur1 = l1
        cur2 = l2
        while cur1 and cur2:
            v = cur1.val + cur2.val + carry
            carry = v // 10
            node = ListNode(v % 10)
            cur.next = node
            cur = node
            cur1 = cur1.next
            cur2 = cur2.next
        
        print(cur1, cur2)
        rem = cur1 if cur1 else cur2
        while rem:
            print(rem)
            v = rem.val + carry
            carry = v // 10
            node = ListNode(v % 10)
            cur.next = node
            cur = node
            rem = rem.next
        
        if carry > 0:
            print(carry)
            cur.next = ListNode(carry)
        return res.next
