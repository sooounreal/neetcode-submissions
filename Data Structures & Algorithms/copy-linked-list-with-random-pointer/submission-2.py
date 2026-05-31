"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # loop over by next, get mapping
        old_to_new = {}
        old = head
        while old:
            new = Node(old.val, None, old.random)
            old_to_new[old] = new
            old = old.next
        
        new = old_to_new[head]
        old = head
        while new:
            if new.random:
                new.random = old_to_new[new.random]
            
            if old.next:
                new.next = old_to_new[old.next]
            new = new.next
            old = old.next
        
        return old_to_new[head]


