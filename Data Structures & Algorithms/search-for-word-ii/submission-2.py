class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        head = TrieNode("", "")
        # create trie
        for word in words:
            cur = head
            for c in word:
                if c in cur.next:
                    cur = cur.next[c]
                else:
                    cur.next[c] = TrieNode(c, "")
                    cur = cur.next[c]
            cur.word = word

        res = set()
        n_rows = len(board)
        n_cols = len(board[0])

        def dfs(r, c, visited, trie):

            if trie.word != "":
                res.add(trie.word)
            
            visited[(r,c)] = 0
            directions = [(-1,0), (1,0), (0,1), (0,-1)]
            for direction in directions:
                dr, dc = direction

                if 0 <= r+dr < n_rows and 0 <= c+dc < n_cols \
                    and (r+dr, c+dc) not in visited and board[r+dr][c+dc] in trie.next:
                        next_char = board[r+dr][c+dc]
                        dfs(r+dr, c+dc, visited, trie.next[next_char])
            visited.pop((r,c))
            return


        for r in range(n_rows):
            for c in range(n_cols):
                if board[r][c] not in head.next:
                    continue
                dfs(r, c, {}, head.next[board[r][c]])

        return list(res)

                
        

class TrieNode:
    def __init__(self, char, word):
        self.char = char
        self.next = {}
        self.word = word