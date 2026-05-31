class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        can_use = [True for _ in range(len(triplets))]
        for i,t in enumerate(triplets):
            a, b, c = t
            if a > target[0] or b > target[1] or c > target[2]:
                can_use[i] = False
        
        max_a = -1
        max_b = -1
        max_c = -1
        for i,t in enumerate(triplets):
            if can_use[i]:
                a, b, c = t
                max_a = max(max_a, a)
                max_b = max(max_b, b)
                max_c = max(max_c, c)
        
        return max_a == target[0] and max_b == target[1] and max_c == target[2]
