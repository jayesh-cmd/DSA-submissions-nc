class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Brute Force ----
        # trip_set = set()
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i]+nums[j]+nums[k] == 0:
        #                 triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
        #                 trip_set.add(triplet)
        # return list(trip_set)
        # T.C. -> O(n cube) -> Three Loops Going n Times
        # S.C. -> O(k) -> where k = number of triplets, O(n square) in worst case

        # Optimal Solution ----
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n):
            if i >0 and nums[i] == nums[i-1]:
                continue

            low, high = i+1, n-1
            while low<high:

                curr_sum = nums[i] + nums[low] + nums[high]
                if curr_sum == 0:
                    result.append([nums[i],nums[low],nums[high]])
                    low+=1
                    high-=1
                    while low<high and nums[low] == nums[low-1]:
                        low+=1
                    while low<high and nums[high] == nums[high+1]:
                        high-=1
                elif curr_sum < 0:
                    low+=1
                else:
                    high-=1
        return result
        # T.C. -> O(n square) -> Two Loops
        # S.C. -> O(1) -> No Extra Space Used