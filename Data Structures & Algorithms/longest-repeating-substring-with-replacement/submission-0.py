class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # Brute --
        # n = len(s)
        # longest = 0
        # for i in range(n):
        #     for j in range(i,n):
        #         substring = s[i:j+1]
        #         freq = {}
        #         for char in substring:
        #             freq[char] = freq.get(char, 0) + 1
        #         max_freq = max(freq.values())
        #         if (j-i+1) - max_freq <= k:
        #             longest = max(longest, j-i+1)
        # return longest
        # Time : O(n cube)
        # Space : O(n)

        # Optimal --
        n = len(s)
        longest = 0
        low = 0
        count = [0] * 26
        for r in range(n):
            count[ord(s[r])-ord('A')] += 1
            while (r-low+1) - max(count) > k:
                count[ord(s[low]) - ord('A')] -= 1
                low+=1
            longest = max(longest, (r-low+1))
        return longest
        # Time : O(n)
        # Space : O(1)