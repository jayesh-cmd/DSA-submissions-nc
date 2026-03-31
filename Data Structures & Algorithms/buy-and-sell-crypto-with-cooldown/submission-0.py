class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0

            if (i, buying) in memo:
                return memo[(i, buying)]

            if buying:
                buy = dfs(i+1, False) - prices[i]
                skip = dfs(i+1, True)
                memo[(i,buying)] = max(buy, skip)

            else:
                sell = dfs(i+2, True) + prices[i]
                skipp = dfs(i+1, False)
                memo[(i, buying)] = max(sell, skipp)

            return memo[(i, buying)]

        return dfs(0, True)