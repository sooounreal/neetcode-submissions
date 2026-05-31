class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            while j < len(nums) - 2: # 2 more elements
                t = target-(nums[i] + nums[j])
                results = self.twoSum(nums, j+1, t)
                for r in results:
                    r = [nums[i], nums[j]] + r
                    res.append(r)
                j += 1
                while j < len(nums) - 2 and nums[j] == nums[j-1]:
                    j += 1
        return res

     

    def twoSum(self, nums, i, target):
        left = i
        right = len(nums) - 1
        res = []
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                res.append([nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
            elif s < target:
                left += 1
            else:
                right -= 1
        return res
