class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        """
        n = 3 
        n-1 = 2 == 2
        n-2 = 1 == 1
        stars(n-2) + stairs(n-1) == 3
        """

        return self.climbStairs(n-1) + self.climbStairs(n-2)
        