class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        tickets.sort(reverse = True)
        adj = defaultdict(list)

        for dep, dest in tickets:
            adj[dep].append(dest)

        res = []

        def dfs(src):

            while src in adj and adj[src]:
                next_src = adj[src].pop()
                dfs(next_src)

            res.append(src)

        dfs("JFK")
        return res[::-1]

        # T.C. -> O(E Log E)
        # S.C. -> O(E)