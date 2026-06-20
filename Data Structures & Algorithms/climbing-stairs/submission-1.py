class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def climbStairsRec(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n in memo:
                return memo[n]
            memo[n] = climbStairsRec(n-1) + climbStairsRec(n-2)

            return memo[n]
        """
        n = 3 
        n-1 = 2 == 2
        n-2 = 1 == 1
        stars(n-2) + stairs(n-1) == 3
        """

        return climbStairsRec(n)
        