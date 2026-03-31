class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # Brute --
        # n = len(nums)
        # dic = {}
        # for num in nums:
        #     dic[num] = dic.get(num,0)+1
        #     if dic[num] > n//2:
        #         return num
        # return -1
        # T.C. -> O(n)
        # S.C. -> O(n)

        # Optimal --
        ans = -1
        count = 0

        for num in nums:
            if count == 0:
                ans = num

            if ans == num:
                count += 1
            else:
                count -= 1

        return ans
        # T.C. -> O(n)
        # S.C. -> O(1)