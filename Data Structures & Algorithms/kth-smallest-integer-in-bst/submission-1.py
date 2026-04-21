# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Brute --
        # values = []
        # def dfs(node):
        #     if not node:
        #         return

        #     values.append(node.val)
        #     dfs(node.left)
        #     dfs(node.right)
        
        # dfs(root)
        # values.sort()

        # for i, value in enumerate(values):
        #     if i + 1 == k:
        #         return value
        # T.C. - O(n log n) due to sorting and S.C. - O(N) array used 

        # Optimal --
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            k-=1
            if k == 0:
                return curr.val

            curr = curr.right