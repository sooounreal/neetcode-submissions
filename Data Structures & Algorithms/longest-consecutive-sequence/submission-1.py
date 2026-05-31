class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        s = set(nums)
        for n in nums:
            cur = 1
            while n+1 in s:
                cur += 1
                n += 1
            res = max(res, cur)
        return res
