class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def backt(i, cur, total):
            # Base Case 1
            if total == target:
                res.append(cur.copy())
                return
            
            # Base Case 2
            if i >= len(nums) or total > target:
                return

            # Include
            cur.append(nums[i])
            backt(i,cur,total+nums[i])

            # Exclude
            cur.pop()
            backt(i+1, cur, total)

        backt(0, [], 0)
        return res

        # T.C. -> O(2^T)
        # S.C. -> O(T)