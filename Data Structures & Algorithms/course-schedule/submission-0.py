class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        premap = {i:[] for i in range(numCourses)}
        for cor, pre in prerequisites:
            premap[cor].append(pre)

        visited = set()
        def dfs(cou):
            if cou in visited:
                return False

            if premap[cou] == []:
                return True

            visited.add(cou)
            for co in premap[cou]:
                if not dfs(co):
                    return False

            visited.remove(cou)
            premap[cou] = []

            return True

        for i in range(numCourses):
            if not dfs(i): return False

        return True