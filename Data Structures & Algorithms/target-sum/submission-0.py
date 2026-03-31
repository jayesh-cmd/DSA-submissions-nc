class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = {}

        def dfs(i, total):
            if i == len(nums):
                if total == target:
                    return 1
                else:
                    return 0

            if (i, total) in memo:
                return memo[(i, total)]

            add = dfs(i+1, total+nums[i])
            sub = dfs(i+1, total-nums[i])

            memo[(i, total)] = add + sub

            return memo[(i, total)]

        return dfs(0, 0)
        # T.C. -> O(N * Sum) 
        # S.C. -> O(N * Sum)