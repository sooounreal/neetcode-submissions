class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for x in nums:
            res = self.bt(x, res)
        return res

    def bt(self, x:int, cur:List[List[int]]) -> List[List[int]]:
        res = []
        for l in cur:
            with_x = l[:]
            without_x = l[:]
            with_x.append(x)
            res.append(with_x)
            res.append(without_x)
        return res