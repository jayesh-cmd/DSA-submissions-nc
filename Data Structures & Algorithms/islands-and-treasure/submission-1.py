class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        q = deque()
        sett = set()

        def addroom(r, c):
            if r<0 or r>=row or c<0 or c>=col or (r,c) in sett or grid[r][c] == -1:
                return

            sett.add((r,c))
            q.append([r,c])

        # Find the Gate
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    q.append([i,j])
                    sett.add((i,j))

        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist

                addroom(r,c+1)
                addroom(r+1,c)
                addroom(r,c-1)
                addroom(r-1,c)

            dist+=1
            

        