class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        row , col = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        # Find the rotten fruit
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh+=1
                elif grid[i][j] == 2:
                    q.append([i,j])

        def rott(r,c):

            nonlocal fresh # Dont want to create a new variable, use the existing once

            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c]!=1:
                return
            grid[r][c] = 2
            fresh -= 1
            q.append((r,c))

        time = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()

                rott(r,c+1)
                rott(r+1,c)
                rott(r,c-1)
                rott(r-1,c)

            time += 1

        if fresh == 0:
            return time
        else:
            return -1

        # T.C. -> O(M * N) where m is rows len and n is column len
        # S.C. -> O(M * N) in worst case there is mostly rotten fruits in the grid

            