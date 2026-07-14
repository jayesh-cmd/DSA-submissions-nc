class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n = len(heights)
        l = 0
        r = n - 1
        max_water = 0

        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            total = width * height

            max_water = max(max_water, total)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_water