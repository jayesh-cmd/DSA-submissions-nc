class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # Brute Force
        # maxx = float('-inf')
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(i, len(nums)):
        #         product *= nums[j]

        #         if product > maxx:
        #             maxx = product
        # return maxx
        # # T.C. -> O(N^2)
        # # S.C. -> O(1)

        # Optimal
        res = max(nums)
        maxx = 1
        minn = 1

        for num in nums:

            prevmax = maxx
            prevmin = minn

            maxx = max(num, prevmax * num, prevmin * num)
            minn = min(num, prevmax * num, prevmin * num)

            res = max(res, maxx)

        return res
        # T.C. -> O(N)
        # S.C. -> O(1)