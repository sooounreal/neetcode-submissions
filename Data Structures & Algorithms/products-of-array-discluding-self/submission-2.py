class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1 , 2, 4, 6]
        # [1 , 1, 2, 8] left
        # [48,24, 6, 1] right

        left = [1 for i in range(len(nums))]
        for i in range(1,len(nums)):
            left[i]  = left[i-1] * nums[i-1]
        print(left)
        right = [1 for i in range(len(nums))]
        for i in range(len(nums)-2,-1,-1):
            right[i] = right[i+1] * nums[i+1]

        res = [left[i] * right[i] for i in range(len(nums))]
        return res