class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s_nums = set(nums)
        cur_max = 0
        for i in range(len(nums)):
            k = nums[i]
            cur = 1
            while k-1 in s_nums:
                cur += 1
                k -= 1
            cur_max = max(cur_max, cur)
        return cur_max


