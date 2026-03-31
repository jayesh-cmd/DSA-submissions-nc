class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        visited = set()
        def dfs(i, prev):
            if i in visited:
                return False

            visited.add(i)

            for j in g[i]:
                if j == prev:
                    continue
                if not dfs(j,i):
                    return False

            return True

        return dfs(0, -1) and n == len(visited)

        