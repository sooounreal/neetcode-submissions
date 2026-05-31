import heapq
import numpy as np
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        def dist(pt):
            x, y = pt[0], pt[1]
            return np.sqrt(x**2 + y**2)
        
        res = []
        heap = [(dist(pt), pt) for pt in points]

        heapq.heapify(heap)
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        
    