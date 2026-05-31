import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        m = {}
        for coord in points:
            x, y = coord[0], coord[1]
            d = x**2 + y**2
            heapq.heappush(heap, d)
            if d in m:
                m[d].append(coord) # [[x,y], [x,y]]
            else:
                m[d] = [coord] # [[x,y]]
        heapq.heapify(heap)
        res = []
        while len(res) < k:
            d = heapq.heappop(heap)
            coords = m[d]
            for c in coords:
                res.append(c)
        return res[:k]
        