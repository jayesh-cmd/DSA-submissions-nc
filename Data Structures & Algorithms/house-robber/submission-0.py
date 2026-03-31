class Solution:
    def rob(self, nums: List[int]) -> int:

        # Brute
        # def solve(i, nums):
        #     if i >= len(nums):
        #         return 0

        #     rob_curr = nums[i] + solve(i+2, nums)
        #     skip_curr = solve(i+1, nums)

        #     return max(rob_curr, skip_curr)

        # return solve(0, nums)

        # Optimal 

        rob1, rob2 = 0,0

        for n in nums:
            temp = max(n + rob1, rob2)

            rob1 = rob2
            rob2 = temp

        return rob2