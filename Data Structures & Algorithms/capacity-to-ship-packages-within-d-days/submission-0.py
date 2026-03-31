class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        # BRUTE ----
        # min_cap = max(weights)
        # max_cap = sum(weights)

        # for cap in range(min_cap, max_cap+1):

        #     days_needed = 1
        #     curr_load = 0

        #     for w in weights:
        #         if curr_load + w > cap:
        #             days_needed += 1
        #             curr_load = 0
        #         curr_load += w

        #     if days_needed <= days:
        #         return cap

        # return max_cap
        # T.C. -> O(N * R), where n is len of weights and r is size of range
        # S.C. -> O(1)

        # Optimal ----

        def canship(capacity):
            days_needed = 1
            curr_load = 0
            for w in weights:
                if curr_load + w > capacity:
                    days_needed += 1
                    curr_load = 0
                curr_load += w
            return days_needed <= days

        left = max(weights)
        right = sum(weights)
        res = right

        while left <= right:
            mid = (left + right) // 2

            if canship(mid):
                res = mid
                right = mid - 1

            else:
                left = mid + 1

        return res
        # T.C. -> O(N • Log(range))
        # S.C. -> O(1)