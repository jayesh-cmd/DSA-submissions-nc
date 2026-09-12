class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        maxarea = 0

        # we put (index, height) in the stack.
        for i, h in enumerate(heights):
            # we pop only when the current height is less than last one in stack.
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxarea = max(maxarea, height * (i - index))
                start = index

            # we append the start index means left side, height
            stack.append((start, h))

        # After all we have remains some index, height in the stack so we calculate the area of them too
        for i, h in stack:
            maxarea = max(maxarea, h * (len(heights) - i))

        return maxarea