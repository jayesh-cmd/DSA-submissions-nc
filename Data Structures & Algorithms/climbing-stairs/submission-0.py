class Solution:
    def climbStairs(self, n: int) -> int:

        # Brute 
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2

        # return self.climbStairs(n-2) + self.climbStairs(n-1)
        # T.C. -> O(2^n) calling function several times
        # S.C. -> O(N) recursion stack

        # Optimal
        if n <= 1:
            return 1

        prev2, prev1 = 1, 1

        for i in range(2, n+1):

            curr = prev2+prev1
            prev2 = prev1
            prev1 = curr

        return curr
        # T.C. -> O(N)
        # S.C. -> O(1)