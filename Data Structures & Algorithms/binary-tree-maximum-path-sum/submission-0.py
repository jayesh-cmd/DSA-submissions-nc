# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.max_path = float('-inf')

        def maxpath(node):
            if not node:
                return 0

            left_gain = max(maxpath(node.left), 0)
            right_gain = max(maxpath(node.right), 0)

            maxscore = node.val + left_gain + right_gain

            self.max_path = max(self.max_path, maxscore)

            return node.val + max(left_gain, right_gain) # When we dont split the node

        maxpath(root)
        return self.max_path
        # T.C. -> O(N)
        # S.C. -> O(H)