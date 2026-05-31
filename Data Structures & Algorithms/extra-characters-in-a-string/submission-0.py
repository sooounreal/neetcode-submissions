class TrieNode:

    def __init__(self, ends=False):
        self.next = {}
        self.ends = ends

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        self.cache = {len(s): 0}
        self.build_trie(dictionary)
        return self.get_extra_chars(s, 0)

    
    def build_trie(self, dictionary):
        self.head = TrieNode()

        for word in dictionary:
            cur = self.head
            for c in word:
                if c not in cur.next:
                    cur.next[c] = TrieNode()
                cur = cur.next[c]
            cur.ends = True
    
    def get_extra_chars(self, s, i):
        if i in self.cache:
            return self.cache[i]
        
        res = 1 + self.get_extra_chars(s, i+1)
        cur = self.head
        for j in range(i, len(s)):
            if s[j] in cur.next:
                cur = cur.next[s[j]]
                if cur.ends:
                    res = min(res, self.get_extra_chars(s, j+1))
            else:
                break

        self.cache[i] = res
        return res
        
