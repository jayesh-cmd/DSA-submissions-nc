class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # Brute --
        # n = len(nums)
        # min_len = float('inf')
        # for i in range(n):
        #     currsum = 0
        #     for j in range(i,n):
        #         currsum += nums[j]
        #         if currsum >= target:
        #             min_len = min(min_len, j-i+1)
        #             break
        # return min_len if min_len != float('inf') else 0
        # T.C. -> O(n square) -> Two Loops Iterating Till n
        # S.C. -> O(1) -> No Extra Space Used

        # Optimal --
        n = len(nums)
        summ = 0
        min_len = float('inf')
        l = 0
        for i in range(n):
            summ += nums[i]
            while summ >= target:
                min_len = min(min_len, i - l + 1)
                summ -= nums[l]
                l += 1
        return min_len if min_len != float('inf') else 0
        # T.C. -> O(n) -> Iterating through array once
        # S.C. -> O(1) -> No extra space used in order to solve this problem
