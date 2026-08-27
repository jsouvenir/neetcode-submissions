class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) # rows
        n = len(matrix[0]) # cols

        l,r = 0, m*n-1

        while l<=r:
            mid = (r + l) // 2

            row = mid // n #integer div to find which row 
            col = mid % n #mod to find the col

            if target > matrix[row][col]: #if target > mid
                l = mid + 1
            elif target < matrix[row][col]:
                r = mid - 1
            elif target == matrix[row][col]:
                return True
        return False