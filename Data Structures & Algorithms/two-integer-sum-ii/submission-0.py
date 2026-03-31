class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Array Is Sorted
        # Brute Force ---- 
        # for i in range(len(numbers)):
        #     for j in range(i+1, len(numbers)):
        #         if numbers[i]+numbers[j] == target:
        #             return [i+1, j+1]
        # return []
        # T.C. -> O(n square) -> Checking Each Pair
        # S.C. -> O(1) -> No Extra Space Used

        # Optimal ---- (Two Pointer)
        left, right = 0, len(numbers)-1

        while left<right:
            curr_sum = numbers[left]+numbers[right]
            if curr_sum == target:
                return [left+1, right+1]
            elif curr_sum < target:
                left+=1
            else:
                right-=1
        return []
        # T.C. -> O(n) -> Going Through Each Element In The Array
        # S.C. -> O(1) -> No Extra Space Used 