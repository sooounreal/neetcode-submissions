class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            # odd
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                res += 1
            # res += 1
            print("odd pal", s[left+1: right])

            # even
            # is_pal = False
            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # is_pal = True
                left -= 1
                right += 1
                res += 1
            # if is_pal:
            #     print("even pal", s[left+1: right])
            #     res += 1
        return res
