import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        char_dict = {}
        heap = []
        for c in s:
            char_dict[c] = char_dict.get(c, 0) + 1
        
        for k, v in char_dict.items():
            heap.append((-v, k))
        
        heapq.heapify(heap)
        if len(s) % 2 == 1 and -heap[0][0] > len(s)/2 + 1:
            return ""
        if len(s) % 2 == 0 and -heap[0][0] > len(s)/2:
            return ""
        
        res = ""

        while heap:
            char_count = heapq.heappop(heap)
            v, char = char_count[0], char_count[1]
            if len(res) > 0 and char == res[-1]:
                next_char_count = heapq.heappop(heap)
                v_next, char_next = next_char_count[0], next_char_count[1]
                res += char_next
                heapq.heappush(heap, (v, char))
                if v_next != -1:
                    heapq.heappush(heap, (v_next+1, char_next))
            else:
                res += char
                if v != -1:
                    heapq.heappush(heap, (v+1, char))
        return res
