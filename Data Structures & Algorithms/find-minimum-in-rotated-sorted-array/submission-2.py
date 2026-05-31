class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left = 0
        right = len(nums) - 1
        while left < right:
            m = (left + right) // 2
            if nums[m] < nums[right]:
                right = m
            else:
                left = m + 1
        return nums[left]

"""
[3,4,1,2]
 l m   r
[2,1]

"""