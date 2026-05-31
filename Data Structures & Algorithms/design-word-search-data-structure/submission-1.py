from collections import deque
class TrieNode:
    def __init__(self, ends=False):
        self.next = {}
        self.ends = ends

class WordDictionary:

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.head
        for s in word:
            if s not in cur.next:
                cur.next[s] = TrieNode()
            cur = cur.next[s]
        cur.ends = True

    def search(self, word: str) -> bool:
        options = deque()
        options.append(self.head)

        for c in word:
            n = len(options)
            for i in range(n):
                cur = options.popleft()
                if c == ".":
                    for key in cur.next:
                        options.append(cur.next[key])
                else:
                    if c in cur.next:
                        options.append(cur.next[c])
            if len(options) == 0:
                return False
        for o in options:
            if o.ends:
                return True
        return False


