import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i in range(k-1):
            heapq.heappush(heap, (-nums[i], i))

        res = []

        for i in range(k-1, len(nums)):
            while heap and heap[0][1] < i-k+1:
                heapq.heappop(heap)
            
            heapq.heappush(heap, (-nums[i], i))
            res.append(-heap[0][0])
        return res
