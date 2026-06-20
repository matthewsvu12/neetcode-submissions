class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        ## reccurence relationship = min(climbStairs(i+1) + cost[i], climbStairs(i+2) + cost[i])
        # cost = [1,2,3]
        # 
        def climbStairs(index):
            if index >= len(cost):
                return 0
            
            return min(climbStairs(index+1) + cost[index], climbStairs(index+2) + cost[index])
        return min(climbStairs(0), climbStairs(1))
            

