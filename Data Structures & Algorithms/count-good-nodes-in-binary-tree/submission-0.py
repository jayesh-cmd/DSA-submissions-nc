# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # Brute -----
        # def dfs(node, path):
        #     if not node:
        #         return 0

        #     isgood = 0
        #     if not path or node.val >= max(path):
        #         isgood = 1

        #     new_path = path + [node.val]

        #     left_count = dfs(node.left, new_path)
        #     right_count = dfs(node.right, new_path)

        #     return isgood + left_count + right_count

        # return dfs(root, [])
        # T.C. -> O(N^2)
        # S.C. -> O(N^2)

        # Optimal ----

        def dfs(node, max_num):
            if not node:
                return 0

            isgood = 0
            if node.val >= max_num:
                isgood = 1

            new_max = max(max_num, node.val)

            isgood += dfs(node.left, new_max)
            isgood += dfs(node.right, new_max)

            return isgood

        return dfs(root, root.val)
        # T.C. -> O(N)
        # S.C. -> O(H)