class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # down = currM + 1
        # right = currN + 1
        # if currN == n and currM == m: path + 1
        # visited
        memo = {}
        def dfs(currM, currN, visited):
            if currM == m-1 and currN == n-1:
                print(1)
                return 1
            if (currM, currN) in memo:
                return memo[(currM, currN)]
            # if (currM, currN) in visited:
            #     return 0
            count = 0
            for x, y in [(1, 0), (0, 1)]:
                if currM + x < 0 or currM + x > (m-1) or currN + y < 0 or currN + y > (n-1) or (currM + x, currN + y) in visited:
                    continue
                visited.add((currM + x, currN + y))
                count += dfs(currM + x, currN + y, visited)
                visited.remove((currM + x, currN + y))
            
            memo[(currM, currN)] = count
            return memo[(currM, currN)]
        return dfs(0, 0, set())

            