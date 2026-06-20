class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        res = []

        # For every cell in the matrix dfs
        # Explore each of it's 4 neighbors <= it's own heights[i]
        # If at the current cell we can reach (0th row or 0th column) and (n-1 row or the n-1 column) then add this cells coordinates to the result list.
        # follow up: 
        # to improve time complexity, as we're visiting cell, we store a Boolean tuple (pacific, atlantic) that will show if we the current can reach both pacific and atlantic
        # incase we encounter a different cell that uses same path of a previously seen cell, then this will allows to prune recursive stack calls.
        #  We OR the Tuple (pacific, atlantic) of the 4 directional dfs calls from every cell 
        def dfs(i, j, visited, seenBoth: tuple) -> Tuple(bool, bool):
            if i < 0 or j < 0 or i >= len(heights) or j >= len(heights[0]) or (i, j) in visited:
                return (False, False)
            # at pacific ocean
            if i == 0 or j == 0:
                seenBoth = (True, seenBoth[1])
            # at atlantic ocean
            if i == len(heights)-1 or j == len(heights[0])-1:
                seenBoth = (seenBoth[0], True)
            if seenBoth[0] and seenBoth[1]:
                return seenBoth
            
            visited.add((i,j))
            seen = seenBoth
            # Check all 4 directions to see if we can reach
            for x, y in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                if i+x < 0 or j+y < 0 or i+x >= len(heights) or j+y >= len(heights[0]) or heights[i][j] < heights[i+x][j+y] or (i+x, j+y) in visited:
                    continue 
                tempP, tempA = dfs(i + x, j + y, visited, seenBoth)
                seen = (tempP or seen[0], tempA or seen[1])
            
            return seen

        # step 1 dfs from every node to find if it can reach both atlantic and pacific oceans
        for m in range(len(heights)):
            for n in range(len(heights[0])):
                pac, at = dfs(m, n, set(), (False, False))
                if pac and at:
                    res.append([m, n])

        return res
