class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        top, left = 0, 0
        right, bottom = len(matrix[0])-1, len(matrix)-1
        res = []
        total = len(matrix[0]) * len(matrix)

        while len(res) < total:
            # left to right
            for col in range(left, right+1):
                res.append(matrix[top][col])
            if len(res) >= total: break
            top += 1

            # top to bottom
            for row in range(top, bottom+1):
                res.append(matrix[row][right])
            if len(res) >= total: break
            right -= 1
            
            # right to left
            for col in range(right, left-1, -1):
                res.append(matrix[bottom][col])
            if len(res) >= total: break
            bottom -= 1

            # bottom to top
            for row in range(bottom, top-1, -1):
                res.append(matrix[row][left])
            if len(res) >= total: break
            left += 1
        
        return res