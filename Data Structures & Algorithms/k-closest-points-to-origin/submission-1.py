import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x,y = point[0], point[1]
            heap.append((x**2+y**2,x,y))
        heapq.heapify(heap)

        res = []
        for i in range(k):
            dist,x,y = heapq.heappop(heap)
            res.append([x,y])
        return res