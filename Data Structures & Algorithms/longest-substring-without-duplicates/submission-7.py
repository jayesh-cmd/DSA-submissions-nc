class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        longest = 1

        for i in range(len(s)):
            for j in range(i+1, len(s)):
                sub = s[i:j+1]
                if len(set(sub)) == len(sub):
                    longest = max(longest, len(sub))
                else:
                    break

        return longest