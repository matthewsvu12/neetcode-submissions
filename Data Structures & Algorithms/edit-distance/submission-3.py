class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # word1 = "monkeys", word2 = "money"
        # m == m
        # o == o
        # n == n
        # k != e (we try inserting e, deleting k, or replacing 'k' w/ 'e')
        # inserting = 1 + dfs("keys", i, j+1, "y") monkeys -> monekeys
        # deleting = 1 + dfs("eys", i+1, j, "ey") monkeys -> moneys
        #  1 + dfs("s", i, j, "")
        # replacing = 1 + dfs("eys", i+1, j+1, "y") monkeys -> moneeys
        # return 0 
        dp = [[math.inf] * (len(word2)+1) for j in range(len(word1)+1)]
        for j in range(len(word2)+1):
            dp[len(word1)][j] = len(word2) - j
        for i in range(len(word1)+1):
            dp[i][len(word2)] = len(word1) - i
        

        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i] != word2[j]:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i+1][j+1], dp[i][j+1])
                else:
                    dp[i][j] = dp[i+1][j+1]
        return dp[0][0]

        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i,j)]
            # all remaining characters in word2 must be inserted
            if i == len(word1):
                return len(word2) - j
            # all remaining characters in word1 must be deleted
            if j == len(word2):
                return len(word1) - i
            dist = 0
            if word1[i] != word2[j]:
                dist = 1 + min(dfs(i, j+1), dfs(i+1, j), dfs(i+1, j+1))
            else:
                dist = dfs(i+1, j+1)
            memo[(i, j)] = dist

            return dist
        return dfs(0, 0)
