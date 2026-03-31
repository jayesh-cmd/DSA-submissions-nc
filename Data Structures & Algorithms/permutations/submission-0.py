class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        sub = []
        n = len(nums)

        def dfs():
            # Base Case
            if len(sub) == n:
                res.append(sub.copy())
                return

            # Check Element And Push & Pop
            for x in nums:
                if x not in sub:
                    sub.append(x)
                    dfs()
                    sub.pop()

        dfs()
        return res

        # T.C. -> O(n!)
        # S.C. -> O(n)