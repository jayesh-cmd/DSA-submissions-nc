class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        row, col = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] != 1:
                return 0
            
            grid[r][c] = 0

            return (1 + 
                    dfs(r, c+1) + 
                    dfs(r+1, c) + 
                    dfs(r, c-1) + 
                    dfs(r-1, c))


        longest = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:

                    cur_area = dfs(i, j)
                    longest = max(longest, cur_area)

        return longest
        # T.C. -> O(M * N) m is the number of rows and n is number of columns
        # S.C. -> O(M * N) recursion stack memory