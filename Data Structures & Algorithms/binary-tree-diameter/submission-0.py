# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # Brute - Force---
        # if not root:
        #     return 0

        # def getheight(node):
        #     if not node:
        #         return 0

        #     return 1 + max(getheight(node.left), getheight(node.right))

        # left_height = getheight(root.left)
        # right_height = getheight(root.right)

        # diameter = left_height + right_height

        # left_subtree_dia = self.diameterOfBinaryTree(root.left)
        # right_subtree_dia = self.diameterOfBinaryTree(root.right)

        # return max(diameter, left_subtree_dia, right_subtree_dia)

        # Optimal ---

        if not root:
            return 0
        
        self.max_diameter = 0

        def getheight(node):
            if not node:
                return 0

            left = getheight(node.left)
            right = getheight(node.right)

            diameter = left + right

            self.max_diameter = max(self.max_diameter, diameter)

            return 1 + max(left, right)

        getheight(root)
        return self.max_diameter