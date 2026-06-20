class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p = 0
        q = len(heights) -1
        maxarea = 0
        while p < q :
            area = (q - p)* min(heights[p], heights[q])
            maxarea = max(area,maxarea)
            if heights[p] < heights[q]:
                p += 1
            else:
                q -=1
        return maxarea 
            