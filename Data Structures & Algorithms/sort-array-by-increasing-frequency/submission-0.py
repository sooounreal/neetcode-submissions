import heapq
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n,0) + 1
        
        sorted_arr = []
        for n in counts:
            sorted_arr.append((counts[n],-n))
        
        sorted_arr.sort()
        
        res = []
        for x in sorted_arr:
            count, num = x[0], -x[1]
            res += [num] * count
        return res
