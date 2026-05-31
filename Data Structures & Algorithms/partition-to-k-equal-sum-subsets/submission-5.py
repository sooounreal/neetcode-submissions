class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False

        target = sum(nums)//k
        nums.sort(reverse=True)
        if max(nums) > target:
            return False

        used = [False for i in range(len(nums))]

        def dfs(i, cur_sum, finished_subsets):
            if finished_subsets == k-1:
                return True
            
            if cur_sum == target:
                return dfs(0, 0, finished_subsets+1)
            elif cur_sum > target:
                return False
            else:
                for j in range(i, len(nums)):
                    if used[j]:
                        continue
                    used[j] = True
                    if dfs(j+1, cur_sum+nums[j], finished_subsets):
                        return True
                    used[j] = False
                    if cur_sum == 0:
                        return False
                return False

        return dfs(0, 0, 0)

            
            