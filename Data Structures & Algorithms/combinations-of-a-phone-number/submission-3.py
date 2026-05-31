class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        char_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        if len(digits) == 0:
            return res

        cur = []
        def dfs(i):
            if i == len(digits):
                res.append("".join(cur))
                return
            
            for char in char_map[digits[i]]:
                cur.append(char)
                dfs(i+1)
                cur.pop()
        
        dfs(0)
        return res
