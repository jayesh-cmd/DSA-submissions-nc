class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Brute --
        # n = len(s)
        # longest = 0
        # for i in range(n):
        #     for j in range(i,n):
        #         current = s[i:j+1]
        #         if len(current) == len(set(current)):
        #             longest = max(longest, len(current))
        # return longest
        # # Time : O(n cube)
        # Space : O(min(n, m)) - Where m = character set size (256 for ASCII)

        # Optimal --
        n = len(s)
        l = 0
        longest = 0
        sett = set()

        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l+=1
            w = (r - l)+1
            longest = max(longest, w)
            sett.add(s[r])
        return longest
        # Time : O(n)
        # Space : O(n)