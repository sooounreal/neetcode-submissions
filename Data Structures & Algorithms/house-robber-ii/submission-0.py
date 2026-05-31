class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # [0, n-2] or [1, n-1]
        rob_first = [0 for i in range(n)]
        rob_last = [0 for i in range(n)]
        rob_first[0] = nums[0]
        rob_first[1] = max(nums[0], nums[1])

        rob_last[-1] = nums[-1]
        rob_last[-2] = max(nums[-1], nums[-2])

        for i in range(2, n-1):
            rob_first[i] = max(nums[i]+rob_first[i-2], rob_first[i-1])
        
        for j in range(n-3, 0, -1):
            rob_last[j] = max(nums[j]+rob_last[j+2], rob_last[j+1])
        
        print(rob_first)
        print(rob_last)
        return max(rob_first[n-2], rob_last[1])