# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # Optimal ( Queue ) ---

        if not root:
            return []

        result = []
        q = collections.deque()
        q.append(root)

        while q:
            level_nodes = []

            for i in range(len(q)):
                node = q.popleft()
                level_nodes.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(level_nodes)

        return result
        # T.C. -> O(N)
        # S.C. -> O(N)