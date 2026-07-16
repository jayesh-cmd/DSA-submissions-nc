class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        if not s:
            return 0

        # longest = 0
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         sub = s[i:j+1]
        #         freq = {}
        #         for char in sub:
        #             freq[char] = freq.get(char, 0) + 1
        #         max_freq = max(freq.values())
        #         needed = len(sub) - max_freq
        #         if needed <= k:
        #             longest = max(longest, len(sub))
        # return longest
        # O(N^2), O(N)

        l = 0
        longest = 0
        n = len(s)
        count = [0] * 26

        for r in range(n):
            count[ord(s[r]) - ord('A')] += 1

            while (r-l+1) - max(count) > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1

            longest = max(longest, (r-l+1))
        return longest