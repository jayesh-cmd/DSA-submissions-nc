class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if not s:
            return ""

        longest = ''
        n = len(s)

        for i in range(n):
            for j in range(i, n):

                sub = s[i : j+1]

                if sub == sub[::-1]:
                    if len(sub) > len(longest):
                        longest = sub

        return longest