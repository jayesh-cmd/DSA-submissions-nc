class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        nums = [1] + nums + [1]
        memo = {}

        def dfs(left, right):
            if left + 1 == right:
                return 0

            if (left, right) in memo:
                return memo[(left, right)]

            max_coins = 0
            for i in range(left + 1, right):
                coins = nums[left] * nums[i] * nums[right]
                total = coins + dfs(left, i) + dfs(i, right)
                max_coins = max(max_coins, total)

            memo[(left, right)] = max_coins
            return max_coins
        
        return dfs(0, len(nums) - 1)
        # T.C. -> O(N ^ 3)
        # S.C. -> O(N ^ 3)