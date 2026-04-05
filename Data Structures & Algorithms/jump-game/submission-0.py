class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        target = n-1

        for i in range(n-1, -1, -1):
            max_reach = nums[i]
            if i + max_reach >= target:
                target = i

        return target == 0

        # T.C. -> O(N)
        # S.C. -> O(1)