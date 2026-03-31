# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # Brute ----
        # if not root:
        #     return True

        # def height(node):
        #     if not node:
        #         return 0
        #     return 1 + max(height(node.left), height(node.right))

        # left_h = height(root.left)
        # right_h = height(root.right)

        # if abs(left_h - right_h) > 1:
        #     return False

        # return self.isBalanced(root.left) and self.isBalanced(root.right)

        # Optimal ---

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            if left == -1: return -1

            right = dfs(node.right)
            if right == -1: return -1

            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        return dfs(root) != -1
