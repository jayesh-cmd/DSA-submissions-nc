class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Brute Force --
        # n = len(nums)
        # for i, num in enumerate(nums):
        #     for j, numm in enumerate(nums):
        #         if num + numm == target:
        #             return [i,j]

        # return []
        # T.C. -> O(n square) -> Checking pair for each
        # S.C. -> O(1) -> No Extra Space Used

        # Optimal Solution --
        need_num = {}

        for i, num in enumerate(nums):
            needed = target - num
            if needed in need_num:
                return [need_num[needed],i]
            need_num[num] = i
        return []
        # T.C. -> O(n) -> iterate through array once
        # S.C. -> O(n) -> that hashmap stores n elements