import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-1*n for n in nums]
        heapq.heapify(heap)
        for i in range(k-1):
            heapq.heappop(heap)
        return -1*heap[0]