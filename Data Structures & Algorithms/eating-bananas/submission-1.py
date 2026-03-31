import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Brute ----
        # n = max(piles)
        # for i in range(1,n+1):
        #     total_hours = 0
        #     for pile in piles:
        #         total_hours += math.ceil(pile/i)
        #     if total_hours<=h:
        #             return i
        # return n
        # T.C. -> O(n * m) -> n is max pile size, m is the number of piles

        # Optimal ----

        left, right = 1, max(piles)
        result = right

        while left <= right:
            mid = (left+right)//2
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile/mid)
            if total_hours <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result
        # T.C. -> O(m log n) -> For log n binary search steps, check all m piles each time