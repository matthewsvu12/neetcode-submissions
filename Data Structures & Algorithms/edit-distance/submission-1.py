class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # word1 = "monkeys", word2 = "money"
        # m == m
        # o == o
        # n == n
        # k != e (we try inserting e, deleting k, or replacing 'k' w/ 'e')
        # inserting = 1 + dfs("keys", i, j+1, "y") monkeys -> monekeys
        # deleting = 1 + dfs("eys", i+1, j, "ey") monkeys -> moneys
        # replacing = 1 + dfs("eys", i+1, j+1, "y") monkeys -> moneeys
        # return 0 

        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i,j)]
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            
            dist = 0
            if word1[i] != word2[j]:
                dist = 1 + min(dfs(i, j+1), dfs(i+1, j), dfs(i+1, j+1))
            else:
                dist = dfs(i+1, j+1)
        
            memo[(i, j)] = dist
            return memo[(i,j)]
        return dfs(0, 0)
