class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        # Brute ---
        # nums.sort()
        # res = []
        # n = len(nums)

        # for i in range(n):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
        #     for j in range(i+1,n):
        #         if j > i+1 and nums[j] == nums[j-1]:
        #             continue
        #         for k in range(j+1,n):
        #             if k > j+1 and nums[k] == nums[k-1]:
        #                 continue
        #             for l in range(k+1,n):
        #                 if l > k+1 and nums[l] == nums[l-1]:
        #                     continue
        #                 summ = nums[i]+nums[j]+nums[k]+nums[l]
        #                 if summ == target:
        #                     res.append([nums[i], nums[j], nums[k], nums[l]])
        # return res
        # T.C. -> O(n^4)
        # S.C. -> O(1)

        # Optimal ---
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1,n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                low, high = j+1, n-1
                while low<high:
                    summ = nums[i]+nums[j]+nums[low]+nums[high]
                    if summ == target:
                        res.append([nums[i], nums[j], nums[low], nums[high]])
                        low += 1
                        high -= 1
                        while low < high and nums[low] == nums[low-1]:
                            low+=1
                        while low < high and nums[high] == nums[high+1]:
                            high-=1
                    elif summ < target:
                        low+=1
                    else:
                        high-=1
        return res
        # T.C. -> O(n^3)
        # S.C. -> O(1)