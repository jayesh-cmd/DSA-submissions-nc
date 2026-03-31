class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Brute Force --
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        # Time Complaxity -> O(n2)
        # Space Complaxity -> O(1)

        # Optimal (use set) --
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        # T.C. -> O(n)
        # S.C. -> O(n)