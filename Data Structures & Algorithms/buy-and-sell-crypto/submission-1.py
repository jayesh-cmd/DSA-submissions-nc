class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minn = float('inf')
        maxx = 0

        for price in prices:
            if price < minn:
                minn = price

            profit = price - minn

            if profit > maxx:
                maxx = profit

        return maxx