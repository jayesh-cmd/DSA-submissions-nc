from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        row, col = len(heights), len(heights[0])
        p_que = deque()
        p_seen = set()
        a_que = deque()
        a_seen = set()

        for i in range(row):
            # Pacific 
            p_que.append((i,0))
            p_seen.add((i,0))

            # Atlantic
            a_que.append((i,col-1))
            a_seen.add((i,col-1))

        for i in range(col):
            
            if (0,i) not in p_seen:
                p_que.append((0,i))
                p_seen.add((0,i))

            if (row-1,i) not in a_seen:
                a_que.append((row-1,i))
                a_seen.add((row-1,i))

        def bfs(que, visited):
            while que:
                r,c = que.popleft()

                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    nr , nc = dr+r, dc+c

                    if nr < 0 or nr >= row or nc < 0 or nc >= col:
                        continue

                    if (nr, nc) in visited:
                        continue

                    if heights[nr][nc] < heights[r][c]:
                        continue

                    visited.add((nr,nc))
                    que.append((nr, nc))

        bfs(p_que, p_seen)
        bfs(a_que, a_seen)

        res = []
        for i in range(row):
            for j in range(col):
                if (i,j) in p_seen and (i,j) in a_seen:
                    res.append([i,j])

        return res