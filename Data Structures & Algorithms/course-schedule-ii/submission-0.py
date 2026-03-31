class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        premap = defaultdict(list)
        for a, b in prerequisites:
            premap[a].append(b)

        state = [0] * numCourses
        order = []

        def dfs(crs):
            if state[crs] == 1:
                return False
            if state[crs] == 2:
                return True

            state[crs] = 1

            for pre in premap[crs]:
                if not dfs(pre):
                    return False

            state[crs] = 2
            order.append(crs)
            return True

        for i in range(numCourses):
            if not dfs(i): return []

        return order