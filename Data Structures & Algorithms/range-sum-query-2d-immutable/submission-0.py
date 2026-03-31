class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        m = len(matrix) # No. of Rows
        n = len(matrix[0]) # Columns

        self.dp = [[0] * (n+1) for _ in range(m+1)] # Adding empty row and column of zeros

        for r in range(m):
            for c in range(n):

                current_val = matrix[r][c]

                top_element = self.dp[r][c+1] # Upper element
                left_element = self.dp[r+1][c] # Left side element
                diagonal_element = self.dp[r][c] # Diagonal element

                self.dp[r+1][c+1] = (current_val + top_element + left_element - diagonal_element)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        return (self.dp[row2+1][col2+1] - 
                self.dp[row1][col2+1] - 
                self.dp[row2 + 1][col1] +
                self.dp[row1][col1])

        # T.C. -> O(1)
        # S.C. -> O(M*N)