class Solution:
    def countSubstrings(self, s: str) -> int:

        # Brute Force Solution
        # res = 0
        # for i in range(len(s)):
        #     for j in range(i, len(s)):

        #         sub = s[i:j+1]

        #         if sub == sub[::-1]:
        #             res += 1
        # return res
        # T.C. -> O(N^3)
        # S.C. -> O(N)

        # Optimal Solution
        res = 0

        def expand_pali(s, l, r):
            res = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res

        for i in range(len(s)):

            res += expand_pali(s, i, i)
            res += expand_pali(s, i, i+1)

        return res
        # T.C. -> O(N^2)
        # S.C. -> O(1)