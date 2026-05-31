class WordDictionary:

    def __init__(self):
        self.head = Node()

    def addWord(self, word: str) -> None:
        cur = self.head
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.ends = True

    def search(self, word: str) -> bool:
        return self.searchFromNode(word, self.head)
    
    def searchFromNode(self, word, node):
        cur = node
        for i, c in enumerate(word):
            if c == ".":
                for k in cur.children:
                    if self.searchFromNode(word[i+1:], cur.children[k]):
                        return True
                return False
            else:
                if c not in cur.children:
                    return False
                cur = cur.children[c]
        return cur.ends
        
class Node:
    def __init__(self):
        self.children = {}
        self.ends = False