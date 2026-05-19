class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        premap = {i:[] for i in range(numCourses)}
        for a, b in prerequisites:
            premap[a].append(b)

        visited = set()

        def dfs(node):
            if node in visited:
                return False
            if premap[node] == []:
                return True

            visited.add(node)
            for nei in premap[node]:
                if not dfs(nei): return False
            visited.remove(node)
            premap[node] = []
            return True

        for i in range(numCourses):
            if not dfs(i): return False
        return True