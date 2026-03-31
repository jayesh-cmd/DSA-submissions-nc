class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # m, n = len(text1), len(text2)
        # def longest(i ,j):
        #     if i == m or j == n:
        #         return 0
        #     if text1[i] == text2[j]:
        #         return 1 + longest(i+1, j+1)
        #     else:
        #         return max(longest(i, j+1), longest(i+1, j))
        # return longest(0,0)
        # # T.C. -> O(2^M*N)
        # # S.C. -> O(M+N)

        m, n = len(text1), len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]
        # T.C. -> O(M*N)
        # S.C. -> O(M*N)