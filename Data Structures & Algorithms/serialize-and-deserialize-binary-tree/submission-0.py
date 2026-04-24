# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    def serialize(self, root: Optional[TreeNode]) -> str:

        values = []

        def dfs(node):
            if not node:
                values.append("N")
                return
            values.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(values)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:

        val = data.split(",")
        self.i = 0

        def dfs():
            if val[self.i] == "N":
                self.i+=1
                return None

            node = TreeNode(int(val[self.i]))
            self.i+=1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()