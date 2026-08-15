class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # res = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         res = max(res, prices[j] - prices[i])

        # return res

        res = 0
        min_price = float('inf')

        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price
            if profit > res:
                res = profit 

        return res