class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        result = []

        while cost:
            min_cost_index, min_cost = min(enumerate(cost), key=lambda x:x[1]);
            min_pairs = []
            for index, value in enumerate(cost):
                if value == min_cost:
                    min_pairs.append(index)
            print(min_pairs)
            max_gas = gas[min_cost_index]
            if len(min_pairs) > 1:
                for i in min_pairs:
                    if gas[i] > max_gas:
                        max_gas = gas[i]
                        min_cost_index = i
            total = total + max_gas - min_cost
            result.append(min_cost_index)
            del cost[min_cost_index]
            del gas[min_cost_index]
        if total < 0 :
            return -1
        return result[0]
            
            
        
            
                