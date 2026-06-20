class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p = 0
        q = len(heights) -1
        maxarea = 0
        while p < q :
            b = q - p
            if heights[p] < heights[q]:
                l = heights [p]
                area = l*b
                p +=1
            else:
                l = heights[q]
                area = l*b
                q -=1
            maxarea = max(area,maxarea)
        return maxarea 
            