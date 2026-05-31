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

        cur = head

        mapping = {}
        while cur:
            new_node = Node(cur.val)
            mapping[cur] = new_node
            cur = cur.next
            
        
        for c in mapping:
            new_node = mapping[c]
            if c.random:
                new_node.random = mapping[c.random]
            if c.next:
                new_node.next = mapping[c.next]
        return mapping[head]
        
        