"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        o2n = {}
        stack = []
        
        cur = node
        while cur not in o2n:
            o2n[cur] = Node(cur.val)
            for n in cur.neighbors:
                if n not in o2n:
                    stack.append(n)
            if stack:
                cur = stack.pop()
            
        
        for old in o2n:
            new = o2n[old]
            new.neighbors = [o2n[n] for n in old.neighbors]
        return o2n[node]
