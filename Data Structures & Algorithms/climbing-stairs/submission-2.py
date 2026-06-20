class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]
        # def climbStairsRec(n):
        #     if n == 1:
        #         return 1
        #     if n == 2:
        #         return 2
        #     if n in memo:
        #         return memo[n]
        #     memo[n] = climbStairsRec(n-1) + climbStairsRec(n-2)

        #     return memo[n]
        # """
        # n = 3 
        # n-1 = 2 == 2
        # n-2 = 1 == 1
        # stars(n-2) + stairs(n-1) == 3
        # """

        # return climbStairsRec(n)
        