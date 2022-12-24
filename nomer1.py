class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res = []
        bSum = 0
        for cost in costs:
            res.append(cost[1] - cost[0])
            bSum += cost[1]
        
        res.sort()
        for index in range(len(res) // 2 , len(res)):
            bSum -= res[index]
        
        return bSum