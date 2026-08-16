class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        longest = 0
        l = 0
        freq = {}

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1

            while (r - l) + 1 - max(freq.values()) > k:
                freq[s[l]] = freq.get(s[l], 0) - 1
                l += 1

            longest = max(longest, (r - l) + 1)

        return longest
            