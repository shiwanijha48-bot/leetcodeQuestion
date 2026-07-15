class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        res = []
        # initalizer pointers for traversal
        top = 0
        left = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1
        # traverse the matrix in spiral order
        while top <= bottom and left <= right:
            for i in range(left, right + 1): # move left to right accross the top row
                res.append(matrix[top][i])
            top += 1
            
            for i in range(top, bottom + 1): # move top to bottomt accross the right col
                res.append(matrix[i][right])
            right -=  1

            if top <= bottom: # move right ot left acrross bottom row, if valid
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            if left <= right: # move to bottom to top along the left column if valid
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res
                
#  tc = o( r * c)
#  sc = o(1)
