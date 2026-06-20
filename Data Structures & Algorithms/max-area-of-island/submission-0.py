class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        def dfs(i, j, visited):
            if i < 0 or j < 0 or i > len(grid)-1 or j > len(grid[0])-1 or grid[i][j] == 0 or (i, j) in visited:
                return 0
            visited.add((i,j))

            res = 0
            for r, c in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                res += dfs(i + r, j + c, visited)
            return 1 + res
        
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == 1:
                    maxArea = max(maxArea, dfs(m, n, set()))
        return maxArea
        