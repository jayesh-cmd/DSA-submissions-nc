class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        s = set(nums)
        longest = 0

        for num in s:
            if num-1 not in s:
                next_time = num+1
                length = 1
                while next_time in s:
                    length += 1
                    next_time += 1
                longest = max(longest, length)
        return longest