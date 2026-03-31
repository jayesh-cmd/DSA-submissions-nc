class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        ROW, COL = len(matrix), len(matrix[0])
        dp = {}

        def dfs(r, c):
            if (r, c) in dp:
                return dp[(r, c)]

            max_path = 1
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                new_row, new_col = r+dr, c+dc

                if (0<= new_row < ROW and
                    0<= new_col < COL and
                    matrix[new_row][new_col] > matrix[r][c]):

                    max_path = max(max_path, 1 + dfs(new_row, new_col))

            dp[(r, c)] = max_path
            return max_path

        hike = 0
        for i in range(ROW):
            for j in range(COL):
                hike = max(hike, dfs(i, j))

        return hike