class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        memo = {}
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            path = 1
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if i + x >= 0 and i + x < len(matrix) and j + y >= 0 and j + y < len(matrix[0]):
                    if matrix[i+x][j+y] > matrix[i][j]:
                        path = max(path, 1 + dfs(i+x, j+y))
            
            memo[(i,j)] = path

            return memo[(i, j)]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i, j)
        
        return max(memo.values())
            
        