class Solution:
    def longestPalindrome(self, s: str) -> str:
        cur_len = 0
        cur_str = ""
        for i in range(len(s)):
            # odd
            left = i
            right = i
            while 0 <= left and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            print('odd', left, right, s[left+1:right], right - left - 1)
            if right - left - 1 > cur_len:
                cur_len = right - left - 1
                cur_str = s[left+1:right]

            # odd
               
            left = i
            right = i+1
            while 0 <= left and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            print('even', left, right, s[left+1:right], right - left - 1)
            if right - left - 1 > cur_len:
                cur_len = right - left - 1
                cur_str = s[left+1:right]
        
        return cur_str