class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Decoding
        1 -> 1, 10, 11, 12, 13, 14.. 19
        2 -> 2, 20, 21, 22, 23, 24, 25, 26
        3 -> 3
        4 -> 4
        5 -> 5
        ....
        9 -> 10

        ex s = 1223
               1, 12
               2, 22
               2, 23
               3
            decode(n+1)
            decode(n+2)
        """
        memo = {}
        def dfs(i):
            if i == len(s):
                return 1
            if i > len(s) or s[i] == '0':
                return 0
            if i in memo:
                return memo[i]
            memo[i] = dfs(i+1)
            if i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and int(s[i+1]) < 7):
                memo[i] += dfs(i+2)
            
            return memo[i]
        return dfs(0)
        