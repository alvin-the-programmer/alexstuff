# https://awwapp.com/b/uqhbahvjpuamr/

class Solution:
    def minCost(self, costs):
        memo = {}
        return self.minCostHelper(0, None, costs, memo)

    def minCostHelper(self, houseNum, lastColor, costs, memo):
        key = (houseNum, lastColor)
        if key in memo:
            return memo[key]

        if houseNum > len(costs) - 1:
            return 0
        
        color_0_cost = costs[houseNum][0] + self.minCostHelper(houseNum + 1, 0, costs, memo) # color0
        color_1_cost = costs[houseNum][1] + self.minCostHelper(houseNum + 1, 1, costs, memo) # color1
        color_2_cost = costs[houseNum][2] + self.minCostHelper(houseNum + 1, 2, costs, memo) # color2
        memo[key] = min(
            float('inf') if lastColor == 0 else color_0_cost,
            float('inf') if lastColor == 1 else color_1_cost, 
            float('inf') if lastColor == 2 else color_2_cost,
        )
        return memo[key]