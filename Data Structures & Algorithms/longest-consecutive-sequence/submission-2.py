class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        longest = 0

        for num in nums:

            curr = num
            count = 1

            while curr + 1 in nums:
                count += 1
                curr += 1
            longest = max(longest, count)

        return longest