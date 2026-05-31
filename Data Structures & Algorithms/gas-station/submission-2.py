class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        min_stop = -1
        

        cur_gas = 0
        total_gas = sum(gas)
        total_cost = sum(cost)
        min_gas = total_gas
        if total_gas < total_cost:
            return -1
        for i in range(len(gas)):
            cur_gas += gas[i] - cost[i]
            if cur_gas < min_gas:
                min_gas = cur_gas
                min_stop = i+1
        return min_stop % len(gas)
        