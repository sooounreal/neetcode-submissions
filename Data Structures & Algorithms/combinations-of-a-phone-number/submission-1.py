class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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

        res = []
        def dfs(i, cur_str):
            if i == len(digits):
                if len(cur_str) > 0:
                    res.append(cur_str)
                return
            
            for char in char_map[digits[i]]:
                dfs(i+1, cur_str+char)
        
        dfs(0, "")
        return res
            