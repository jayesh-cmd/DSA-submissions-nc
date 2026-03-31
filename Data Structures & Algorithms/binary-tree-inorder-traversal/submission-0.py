# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []

        def dfs(node):

            if not node:
                return

            dfs(node.left)

            result.append(node.val)

            dfs(node.right)

        dfs(root)
        return result

        # Time Complexity: O(N) where N is the total number of nodes, If you have 10 nodes, you do 10 units of work. If you have 1 million, you do 1 million. This is linear: $O(N)$.
        # Space Complexity: Imagine a tree that is just a straight line (Linked List style): 1 -> 2 -> 3 -> 4, To reach Node 100, the computer has to keep Paper #1, #2, #3... #99 all sitting on the desk "paused", waiting for the bottom to return.