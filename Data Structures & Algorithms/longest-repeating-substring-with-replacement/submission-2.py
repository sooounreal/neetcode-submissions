class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        chars = {}
        res = 0

        for right in range(len(s)):
            chars[s[right]] = chars.get(s[right], 0) + 1
            while not self.can_work(chars, k):
                chars[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
            print(s[left:right+1], res)
        return res
    

    def can_work(self, chars, k):
        max_count = max(chars.values())
        total_count = sum(chars.values())
        return total_count - max_count <= k
