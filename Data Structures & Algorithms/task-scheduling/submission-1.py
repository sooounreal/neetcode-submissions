import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for t in tasks:
            freq[t] = freq.get(t, 0) + 1
        print(freq)
        heap = []
        for t in freq:
            heapq.heappush(heap, (-freq[t], t))

        heapq.heapify(heap)
        print(heap)
        res = 0
        while heap:
            used = []
            for i in range(n+1):
                res += 1
                if not heap:
                    continue
                f, t = heapq.heappop(heap)
                freq[t] -= 1
                print(res, t, freq[t])
                used.append(t)
                if freq[t] == 0:
                    freq.pop(t)
                    used.pop()
                if not freq:
                    return res
            for t in used:
                heapq.heappush(heap, (-freq[t], t))
            print("new heap", heap)
        return res
                
            


