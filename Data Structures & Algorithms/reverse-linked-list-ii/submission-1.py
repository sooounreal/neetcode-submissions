# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 1 -> 2 -> 3 -> 4 -> 5
# p    c    n

#      p    c    n
# 1 -> 3 -> 2 -> 4 -> 5
#           p    c    n
# 1 -> 4 -> 3 -> 2 -> 5
# 1 -> 4 -> 3 -> 2 -> 5
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        l_node = head
        prev = None
        for i in range(left-1):
            prev = l_node
            l_node = l_node.next
        
        r_node = l_node

        for i in range(right-left+1):
            r_node = r_node.next
        # print(l_node.val, r_node.val)
        h = self.reverse(l_node, r_node)
        if prev:
            prev.next = h
            return dummy.next
        else:
            return h
        

    def reverse(self, head, tail):
        prev = None
        cur = head
        while cur != tail:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        head.next = tail
        return prev
    

