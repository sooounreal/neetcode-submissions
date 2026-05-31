class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                res += self.twoSum(i+1, nums, -nums[i])
        return res
            

    def twoSum(self, i, nums, target):
        left = i
        right = len(nums) - 1
        res = []
        while left < right:
            if nums[left] + nums[right] == target:
                res.append([-target, nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
        print(target, res)
        return res

# [-4, -1, -1, 0, 1, 2]

# [-1,-1,-1,1,1,2,3]