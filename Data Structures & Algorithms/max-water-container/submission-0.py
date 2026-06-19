class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            area = 0
            for j in range(i + 1, len(heights)):
                if heights[i] > heights[j] :
                    curr = heights[j] * (j-i)
                    area = max(curr,area)
                elif heights[i] <= heights[j] :
                    curr = heights[i] * (j-i)
                    area = max(curr,area)
            max_area = max(area,max_area)
        return max_area
