from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        maxheap = [-cnt for cnt in count.values()]
        heapq.heapify(maxheap)

        time = 0
        q = deque()

        while maxheap or q:
            time += 1

            if maxheap:
                element = 1 + heapq.heappop(maxheap)
                if element:
                    q.append([element, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])

        return time
        # T.C. -> O(Total Cycle)
        # S.C. -> O(1)