class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for c in tasks:
            counts[c] = counts.get(c, 0) + 1
        print(counts)
        heap = []
        for c in counts:
            count = counts[c]
            heapq.heappush(heap, (-count, c))
        print(heap)
        cd = {}
        res = 0
        while heap:
            res += 1

            popped = []
            for i in range(len(heap)):
                top_count, char = heapq.heappop(heap)
                if char not in cd:
                    if -top_count > 1:
                        popped.append((top_count+1, char))
                    cd[char] = n + 1
                    break
                else:
                    popped.append((top_count,char))
            for t in popped:
                top_count, char = t
                heapq.heappush(heap, (top_count, char))
            
            # decrease everythings cd by 1
            chars = list(cd.keys())
            for c in chars:
                cd[c] -= 1
                if cd[c] == 0:
                    cd.pop(c)
            print(cd, heap)
        
        return res
            