import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        g = defaultdict(list)
        for s, ti, time in times:
            g[s].append((ti, time))

        min_heap = [(0, k)]
        sett = set()
        longest = 0

        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in sett:
                continue

            sett.add(node)
            longest = max(longest, time)
            for no, t in g[node]:
                if no not in sett:
                    heapq.heappush(min_heap, (t + time, no))

        if len(sett) == n:
            return longest
        else:
            return -1