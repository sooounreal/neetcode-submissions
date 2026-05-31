class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        # freq = {1:1, 2:1}
        print('freq', freq)
        reverse = {}
        for kk in freq.keys():
            if freq[kk] in reverse:
                reverse[freq[kk]].append(kk)
            else:
                reverse[freq[kk]] = [kk]
        print('rev',reverse)
        # reverse = {1:[1,2]}
        keys = sorted(reverse.keys(), reverse=True)
        print('keys',keys)
        res = []
        for i in range(k):
            res += reverse[keys[i]]
            print(res)
            if len(res) == k:
                return res

        