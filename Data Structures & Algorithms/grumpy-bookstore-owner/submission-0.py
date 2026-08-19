class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        baseline = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                baseline += customers[i] 
        
        max_extra = 0
        cur_sum = 0
        for i in range(minutes-1):
            cur_sum += customers[i]*grumpy[i]
        
        for i in range(minutes-1, len(grumpy)):
            cur_sum += customers[i]*grumpy[i]
            max_extra = max(max_extra, cur_sum)
            cur_sum -= customers[i-minutes+1] * grumpy[i-minutes+1]
        return max_extra+baseline


        # [1,2,3,4,5]
