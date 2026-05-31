# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # h
        # 1 -> 2 -> 3 -> 4 -> 5 -> 6
        # 3 -> 2 -> 1 -> 4 -> 5 -> 6
        # get end of cur group - cur_end
        # get start of next group - cur_end.next
        res = ListNode(0, head)
        start = head
        cur = head
        prev = res
        while start:
            cur = start
            for i in range(k-1):
                cur = cur.next
                if not cur:
                    return res.next
            cur_end = cur
            
            # swap within k group
            next_start = cur_end.next
            prev.next = self.reverse(start,k)
            start.next = next_start
            prev = start

            start = next_start
        return res.next


    def reverse(self, head, k):
        prev = None
        cur = head
        for i in range(k):
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        return prev
        


            
            