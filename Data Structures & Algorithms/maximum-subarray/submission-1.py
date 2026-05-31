class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max = -1000
        cur_sum = 0
        l = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            cur_max = max(cur_max, cur_sum)
            cur_sum = max(cur_sum, 0)
                
        return cur_max