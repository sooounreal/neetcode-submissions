import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        my_heap = []
        for n in nums:
            heapq.heappush(my_heap, -n)
        
        for i in range(k):
            res = heapq.heappop(my_heap)
        
        return -res