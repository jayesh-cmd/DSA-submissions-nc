class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Brute Force
        # res = []
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             product *= nums[j]
        #     res.append(product)
        # return res
        # T.C. -> O(n^2)
        # S.C. -> O(1), res didnt count as extra space , given in the question

        # Optimal 
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
        # T.C. -> O(N)
        # S.C. -> O(1)