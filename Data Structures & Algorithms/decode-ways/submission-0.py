class Solution:
    def numDecodings(self, s: str) -> int:
        
        # # Recursive
        # def dfs(i):
        #     if i == len(s):
        #         return 1

        #     if s[i] == '0':
        #         return 0

        #     res = dfs(i+1) # if we take 0 the index now from where to start it's i+1, taken 1 digit
        #     if i + 1 < len(s):
        #         if s[i] == '1' or (s[i] == '2' and s[i+1] in '0123456'):
        #             res += dfs(i+2) # if we tak 0,1 index now from where to start it's i+2, taken 2 digits
        #     return res
        # return dfs(0)
        # # T.C. -> O(2^N)
        # # S.C. -> O(N)

        # Memoization

        dp = {len(s) : 1}

        def solve(i):

            if i in dp:
                return dp[i]

            if s[i] == '0':
                return 0

            res = solve(i+1)

            if i+1 < len(s):
                if s[i] == '1' or (s[i] == '2' and s[i+1] in '0123456'):
                    res += solve(i+2)
                
            dp[i] = res
            return res

        return solve(0)
        # T.C. -> O(N)
        # S.C. -> O(N)