class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # # Better --
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return num
        #     seen.add(num)
        # return -1
        # # T.C. -> O(n)
        # # S.C. -> O(n)

        # Optimal -- Floyd Or Two Pointer
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
        # T.C. -> O(n)
        # S.C. -> O(1)