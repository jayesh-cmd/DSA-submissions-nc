class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        temp = temperatures
        n = len(temp)
        stack = []
        res = [0] * n

        for i , t in enumerate(temp):
            while stack and stack[-1][0] < t:
                stack_t, stack_i = stack.pop()
                res[stack_i] = i - stack_i

            stack.append((t, i))

        return res