class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        global_max = nums[0]
        cur_max = nums[0]

        for i in range(1, len(nums)):
            cur_max = max(nums[i], cur_max + nums[i])
            global_max = max(global_max, cur_max)
        return global_max