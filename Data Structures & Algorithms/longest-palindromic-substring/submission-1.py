class Solution:
    def longestPalindrome(self, s: str) -> str:

        # Brute Force ( Sliding window )
        # if not s:
        #     return ""

        # longest = ''
        # n = len(s)

        # for i in range(n):
        #     for j in range(i, n):

        #         sub = s[i : j+1]

        #         if sub == sub[::-1]:
        #             if len(sub) > len(longest):
        #                 longest = sub
        # return longest
        # T.C. -> O(N^3)
        # S.C. -> O(N)

        # Optimal 

        res = ''

        for i in range(len(s)):

            l,r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > len(res):
                    res = s[l:r+1]
                l-=1
                r+=1

            l,r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > len(res):
                    res = s[l:r+1]
                l-=1
                r+=1

        return res
        # T.C. -> O(N^2)
        # S.C. -> O(N)