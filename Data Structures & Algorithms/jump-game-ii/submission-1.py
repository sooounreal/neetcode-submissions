class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = [0 for _ in range(len(nums))]

        for i in range(len(nums)-2, -1, -1):
            min_steps = len(nums)
            for j in range(1, nums[i]+1):
                if i+j > len(nums) - 1:
                    break
                min_steps = min(min_steps, 1+steps[i+j])
            
            steps[i] = min_steps
        
        return steps[0]