class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        sol = []
        nums.sort()

        def dfs(i):
            # Base Case
            if i >= len(nums):
                res.append(sol[:])
                return

            # Include , nums[i]
            sol.append(nums[i])
            dfs(i+1)
            sol.pop()

            # Include , Without nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1)

        dfs(0)
        return res
        # T.C. -> O(n · 2^n) , where n is len of subsets and 2^n is the number of subsets
        # S.C. -> O(n) , Due to recursion stack