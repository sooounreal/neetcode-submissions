import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0], 0, 0)]
        visited = set()

        directions = [(1,0), (-1,0), (0,-1), (0,1)]
        while heap:
            cur_max, r, c = heapq.heappop(heap)
            print(r,c,cur_max)
            if r == len(grid)-1 and c == len(grid)-1:
                return cur_max
            visited.add((r,c))
            for dr, dc in directions:
                if dr+r < 0 or dr+r > len(grid)-1 or dc+c < 0 or dc+c > len(grid)-1:
                    continue
                elif (dr+r, dc+c) in visited:
                    continue
                next_min = max(cur_max, grid[dr+r][dc+c])
                heapq.heappush(heap, (next_min, dr+r, dc+c))
        

