class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # Brute Force Method:
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i] == nums[j] and abs(i-j) <= k:
        #             return True
        # return False
        # T.C. - O(n2) -> You are checking every pair of indices, so two loops over the array.
        # S.C. - O(1)


        # Optimal Solution
        seen = {}
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i
        return False
        # T.C. - O(n) - Scan array only once
        # S.C - O(n) - every numbers last index