# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        mapp = {val:i for i, val in enumerate(inorder)}
        self.idx = 0

        def helper(left, right):
            if left > right:
                return None

            root_val = preorder[self.idx]
            root = TreeNode(root_val)
            self.idx += 1

            mid = mapp[root_val]

            root.left = helper(left, mid-1)
            root.right = helper(mid+1, right)

            return root

        return helper(0, len(inorder)-1)