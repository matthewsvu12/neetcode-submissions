class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        ## reccurence relationship = min(climbStairs(i+1) + cost[i], climbStairs(i+2) + cost[i])
        # cost = [1,2,3]
        memo = {}
        def climbStairs(index):
            if index >= len(cost):
                return 0
            if index in memo:
                return memo[index]
                
            memo[index] = min(climbStairs(index+1) + cost[index], climbStairs(index+2) + cost[index])

            return memo[index]
        return min(climbStairs(0), climbStairs(1))
            

