class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 1
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        
        if int(s[:2]) <= 26:
            return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
        else:
            return self.numDecodings(s[1:])