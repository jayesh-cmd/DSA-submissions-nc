class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
       
        row, col = len(grid), len(grid[0])
        sett = set()
        q = deque()

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    sett.add((i,j))
                    q.append([i,j])

        def chest(r,c):
            if r<0 or r>=row or c<0 or c>=col or (r,c) in sett or grid[r][c]==-1:
                return

            grid[r][c] = 0
            sett.add((r,c))
            q.append([r,c])

        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist

                chest(r,c+1)
                chest(r+1,c)
                chest(r,c-1)
                chest(r-1,c)

            dist += 1