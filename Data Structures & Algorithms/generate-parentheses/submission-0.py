class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        sub = []

        def dfs(openn, closee):
            # Base Case
            if len(sub) == 2*n:
                res.append("".join(sub))
                return

            # Open Bracket
            if openn < n:
                sub.append("(")
                dfs(openn+1, closee)
                sub.pop()

            # Close Bracket
            if closee < openn:
                sub.append(")")
                dfs(openn, closee+1)
                sub.pop()

        dfs(0, 0)
        return res
        # T.C. -> O(2**n)
        # S.C. -> O(n)