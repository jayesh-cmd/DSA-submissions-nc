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
            # Base Case
            if node in oldtonew:
                return oldtonew[node]

            copy = Node(node.val)
            oldtonew[node] = copy

            for nie in node.neighbors:
                copy.neighbors.append(dfs(nie))

            return copy

        return dfs(node) if node else None
        # T.C. -> O(n), O(V + E) where v is vertices we are visiting each vertices and e is edges
        # S.C. -> O(V + E), storing into hash map