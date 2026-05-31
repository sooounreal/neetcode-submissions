class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        res = 0
        seen = set()
        cur = 0
        for right in range(len(s)):
            if s[right] not in seen:
                
                seen.add(s[right])
                print("adding ", s[right], seen)
            else:
                print("s[right]", s[right])
                while s[left] != s[right]:
                    print('remove', s[left], s[right])
                    seen.remove(s[left])
                    left += 1
                left += 1
                print("left is now ",s[left])
                

            cur = right - left + 1 
            res = max(res, cur)
        return res