class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        max_including = nums[0]
        global_max = nums[0]
        min_including = nums[0]
        global_min = nums[0]

        
        for i in range(1, len(nums)):
            max_including = max(max_including+nums[i], nums[i])
            global_max = max(global_max, max_including)

            min_including = min(min_including+nums[i], nums[i])
            global_min = min(global_min, min_including)

        if sum(nums) - global_min != 0:
            return max(global_max, sum(nums) - global_min)
        else:
            return global_max
        

