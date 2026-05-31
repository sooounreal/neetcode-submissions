import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-1 * s for s in stones]
        heapq.heapify(heap)
        while len(heap) >= 2:
            x = -1 * heapq.heappop(heap)
            y = -1 * heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, y-x)
        if heap:
            return -1*heap[0]
        else:
            return 0