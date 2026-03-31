class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Brute --
        # n = len(prices)
        # max_pf = 0
        # for i in range(n):
        #     for j in range(i+1,n):
        #         pf = prices[j] - prices[i]
        #         max_pf = max(max_pf, pf)
        # return max_pf
        # T.C. -> O(N^2) -> for each day we are checking pair
        # S.C. -> O(1)

        # Optimal --
        n = len(prices)
        max_pf = 0
        min_price = float('inf')

        for i in range(n):
            min_price = min(min_price, prices[i])
            pf = prices[i] - min_price
            max_pf = max(max_pf, pf)

        return max_pf
        # T.C. -> O(n)
        # S.C. -> O(1)