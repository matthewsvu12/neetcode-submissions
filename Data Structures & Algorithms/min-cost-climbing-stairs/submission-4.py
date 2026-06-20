class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        dp = [-1] * (n+1)

        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[n-1], dp[n-2])

        ## reccurence relationship = min(climbStairs(i+1) + cost[i], climbStairs(i+2) + cost[i])
        # cost = [1,2,3]
        # memo = {}
        # def climbStairs(index):
        #     if index >= len(cost):
        #         return 0
        #     if index in memo:
        #         return memo[index]

        #     memo[index] = + cost[index] + min(climbStairs(index+1), climbStairs(index+2))

        #     return memo[index]
        # return min(climbStairs(0), climbStairs(1))
            

