class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        answer = [1] * n

        #left
        l = 1
        for i in range(n):
            answer[i] = l
            l *= nums[i]

        #right
        r = 1
        for i in range(n-1, -1, -1):
            answer[i] *= r
            r *= nums[i]

        return answer