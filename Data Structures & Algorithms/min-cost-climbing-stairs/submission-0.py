class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        prev = 0
        curr = 0

        for i in range(2, len(cost) + 1):

            two_step = prev + cost[i-2]
            one_step = curr + cost[i-1]

            new_cost = min(two_step, one_step)

            prev = curr
            curr = new_cost

        return curr

        # T.C. -> O(N)
        # S.C. -> O(1)