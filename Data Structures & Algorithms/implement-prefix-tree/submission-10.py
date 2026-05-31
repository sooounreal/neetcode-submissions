class Node:
    def __init__(self, val, ends=False):
        self.val = val
        self.next = {}
        self.ends = ends

class PrefixTree:

    def __init__(self):
        self.next = {}

    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.next:
                cur.next[c] = Node(c)
            cur = cur.next[c]
        cur.ends = True

    def search(self, word: str) -> bool:
        cur = self
        for c in word:
            if c not in cur.next:
                return False
            cur = cur.next[c]
        return cur.ends

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for c in prefix:
            if c not in cur.next:
                return False
            cur = cur.next[c]
        return True

        
        