class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if len(sub) == len(set(sub)):
                    longest = max(longest, j-i+1)

        return longest