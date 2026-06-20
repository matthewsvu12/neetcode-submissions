class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        fresh = 0
        rotten = 0
        total = 0
        q = deque()
        minutes = 0
        # 1. find all the rotten fruit to visit and number of fresh
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                # rotten fruit we visit its neighbors
                if grid[m][n] == 2:
                    q.append((m, n))
                    total += 1
                elif grid[m][n] == 1:
                    fresh += 1
                    total += 1
        if fresh == 0:
            return 0
        # 2. bfs every rotten fruit and increment the minutes it takes to do at
        # every iteration of the bfs 
        while q:
            minutes += 1
            for i in range(len(q)):
                cell = q.popleft()
                if grid[cell[0]][cell[1]] == 1:
                    rotten += 1
                grid[cell[0]][cell[1]] = 2
                for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
                    if (cell[0]+x < 0 or cell[0]+x > len(grid)-1
                     or cell[1]+y < 0 or cell[1]+y > len(grid[0])-1 
                     or grid[cell[0]+x][cell[1]+y] == 0 or grid[cell[0]+x][cell[1]+y] == 2):
                        continue
                    # print(cell[0]+x, cell[1]+y)
                    q.append((cell[0]+x, cell[1]+y))
        print(minutes)
                    
        print(fresh, rotten, total)

        return -1 if rotten != fresh else minutes-1