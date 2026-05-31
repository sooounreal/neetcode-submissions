class PrefixTree:

    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        print("insert", word)
        cur = self.head
        for c in word:
            if c not in cur.child:
                cur.child[c] = Node()
            cur = cur.child[c]
        cur.ends = True


    def search(self, word: str) -> bool:
        cur = self.head
        for c in word:
            if c not in cur.child:
                return False
            cur = cur.child[c]
        return cur.ends

    def startsWith(self, prefix: str) -> bool:
        cur = self.head
        for c in prefix:
            if c not in cur.child:
                return False
            cur = cur.child[c]
        return True
        
class Node:

    def __init__(self):
        self.ends = False
        self.child = {}  # {char: Node}