class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        counts = {"R":0, "D":0}
        lost = set()
        neg = {"R":0, "D":0}

        while True:
            for i, sen in enumerate(senate):
                if i in lost:
                    continue
                if neg[sen] > 0:
                    print("lost", i, sen)
                    lost.add(i)
                    counts[sen] += 1
                    neg[sen] -= 1
                else:
                    counts[sen] += 1
                    other = "R" if sen == "D" else "D"
                    counts[other] -= 1
                    neg[other] += 1
                    print("cancelling", i, sen, counts)
            print(counts)
            if counts["R"] <= 0:
                return "Dire"
            if counts["D"] <= 0:
                return "Radiant"


            
