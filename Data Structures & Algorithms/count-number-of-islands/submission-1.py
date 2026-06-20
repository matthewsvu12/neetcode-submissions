class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = set()
        count = 0
        def dfs(r, c):
            if r < 0 or r > len(grid) - 1 or c < 0 or c > len(grid[0]) - 1 or (r, c) in visited or grid[r][c] == '0':
                return
            visited.add((r, c))

            for i, j in dirs:
                dfs(i + r, j + c)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and (row, col) not in visited:
                    count += 1
                    dfs(row, col)
        return count
        