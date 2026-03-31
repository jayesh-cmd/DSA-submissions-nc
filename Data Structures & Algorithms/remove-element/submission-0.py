class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # Brute Force ----
        # temp = []
        # for num in nums:
        #     if num != val:
        #         temp.append(num)

        # for i in range(len(temp)):
        #     nums[i] = temp[i]
        # return len(temp)
        # T.C. -> O(n) Travering The Array Twice
        # S.C. -> O(n) Used Temp As Extra Space

        # Optimal Solution ----
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
               nums[j] = nums[i]
               j += 1
        return j
        # T.C.-> O(n) - Single Pass Through Array
        # S.C. -> O(1) - No Extra Space Used 