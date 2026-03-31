class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        row, col = len(grid), len(grid[0])
        sett = set()
        q = deque()

        def godir(r, c):
            if r<0 or r>=row or c<0 or c>=col or (r,c) in sett or grid[r][c] == -1:
                return

            sett.add((r,c))
            q.append([r,c])

        # Find The Gate And put them in set and q
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    sett.add((i,j))
                    q.append([i,j])

        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist

                godir(r,c+1)
                godir(r+1,c)
                godir(r,c-1)
                godir(r-1,c)

            dist+=1
            # T.C. -> O(M * N) where m is rows and n is columns and we iterate through whole grid once to find the gate
            # S.C. -> O(M * N) cos we used set and q 