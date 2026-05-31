class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod_left = [1 for i in range(n)]
        prod_right =  [1 for i in range(n)]

        for i in range(1, n):
            prod_left[i] = prod_left[i-1] * nums[i-1]
            r = n - 1 - i 
            prod_right[r] = prod_right[r+1] * nums[r+1]
        
        print(prod_left)
        print(prod_right)
        output = []
        for i in range(n):
            output.append(prod_left[i] * prod_right[i])
        return output
