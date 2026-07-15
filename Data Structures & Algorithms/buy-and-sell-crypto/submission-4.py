class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         prof = prices[j] - prices[i]
        #         profit = max(profit, prof)
        # return profit
        # O(N^2), O(1)

        min_price = float('inf')
        max_profit = 0

        for price in prices:

            if price < min_price:
                min_price = price

            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit 