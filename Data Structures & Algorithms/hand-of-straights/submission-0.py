class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if len(hand) % n != 0:
            return False
        
        counts = {}
        for c in hand:
            counts[c] = counts.get(c, 0) + 1
        
        keys = list(counts.keys())
        keys.sort()
        removed = set()
        i = 0
        while i < len(keys):
            k = keys[i]
            if k in removed:
                i += 1
                continue
            groups = counts[k]
            for j in range(groupSize):
                # print(k, groups, k+j)
                if k+j not in counts:
                    return False
                counts[k+j] -= groups
                if counts[k+j] < 0:
                    return False
                elif counts[k+j] == 0:

                    removed.add(k+j)
            i += 1
        return True

            