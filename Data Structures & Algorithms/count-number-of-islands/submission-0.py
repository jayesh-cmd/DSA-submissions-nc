class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row, col = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] != '1':
                return

            else:
                grid[r][c] = 0
                dfs(r, c+1)
                dfs(r+1, c)
                dfs(r, c-1)
                dfs(r-1, c)

        island = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    island += 1
                    dfs(i, j)
            
        return island
        # T.C. -> O(M * N) where M is the number of rows and N is the number of columns
        # S.C. -> O(M * N)