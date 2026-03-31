"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        oldtonew = {}

        def dfs(node):
            if node in oldtonew:
                return oldtonew[node]

            copy = Node(node.val)
            oldtonew[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node) if node else None

        # T.C. -> O(V + E) where v is vertices and e is edges
        # S.C. -> O(V) we are storing copy of vertices