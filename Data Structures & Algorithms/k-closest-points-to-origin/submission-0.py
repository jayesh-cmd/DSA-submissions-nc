import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        close = []
        for x, y in points:
            dist = ((x*x) + (y*y))
            close.append([dist, x, y])

        heapq.heapify(close)

        res = []
        for i in range(k):
            dist, x, y = heapq.heappop(close)
            res.append([x, y])

        return res
        # T.C. ->   O(N Log K)
        # S.C. -> O(N)