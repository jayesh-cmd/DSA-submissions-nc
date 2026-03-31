class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # # Recursive
        # def dfs(r, c):
        #     if r == m-1 and c == n-1:
        #         return 1
        #     if r>=m or c >= n:
        #         return 0
        #     down = dfs(r, c+1)
        #     right = dfs(r+1, c)
        #     return down + right
        # return dfs(0,0)
        # # T.C. -> O(2^M+N), S.C. -> O(M+N)

        # Optimal
        row = [1] * n

        for i in range(m-1):
            newrow = [1] * n
            for j in range(n-2, -1, -1):
                newrow[j] = newrow[j+1] + row[j]
            row = newrow
        return row[0]
        # O(M*N)
        # O(N)