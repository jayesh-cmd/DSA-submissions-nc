class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_water = 0

        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                curr = (j-i) * min(heights[i], heights[j])
                max_water = max(curr, max_water)

        return max_water