class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []

        def backtrack(i):

            if i >= len(nums):
                res.append(subset.copy())
                return

            # Include The Number
            subset.append(nums[i])
            backtrack(i + 1)

            # Exclude The Number
            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return res

        # T.C. -> O(N • 2^n)
        # S.C. -> O(N)