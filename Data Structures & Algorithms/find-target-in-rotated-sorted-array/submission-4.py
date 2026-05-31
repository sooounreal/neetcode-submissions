class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                    return mid
            # left sorted
            if nums[left] < nums[mid]:
                if target == nums[left]:
                    return left
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # right sorted
                if target == nums[right]:
                    return right
                if target > nums[right] or target < nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
                    
                
                
