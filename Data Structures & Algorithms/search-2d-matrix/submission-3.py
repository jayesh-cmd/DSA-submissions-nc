class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row = len(matrix)
        col = len(matrix[0])
        total = row * col
        l = 0
        r = total - 1

        while l <= r:
            mid = (l + r) // 2
            row_ = mid // col
            col_ = mid % col

            specific = matrix[row_][col_]

            if target == specific:
                return True

            elif target > specific:
                l = mid + 1
            else:
                r = mid - 1

        return False