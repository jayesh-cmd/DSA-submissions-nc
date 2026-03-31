class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        # Brute ---
        # n = len(nums)
        # k = k % n
        # temp = nums.copy()
        # for i in range(n):
        #     new_pos = (i+k) % n
        #     nums[new_pos] = temp[i]
        # return nums
        # T.C. -> O(n) -> Iterate through whole array
        # S.C. ->  O(n) -> Array copy in temp

        # Optimal ---
        n = len(nums)
        k = k % n

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(0, n-1) # Reverse Whole Array
        reverse(0, k-1) # Reverse First k elements
        reverse(k, n-1) # Reverse remaining elements
        
        return nums
        # T.C. -> O(n)
        # S.C. -> O(1)