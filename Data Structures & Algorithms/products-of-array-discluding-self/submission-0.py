class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left = [1, 1, 2, 8]
        # right= [48, 24, 6, 1]

        n = len(nums)
        left = [1 for i in range(n)]
        right = [1 for i in range(n)]
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
        
        for j in range(n - 2, -1, -1):
            right[j] = right[j+1] * nums[j+1]
        
        output = [left[i] * right[i] for i in range(n)]
        return output