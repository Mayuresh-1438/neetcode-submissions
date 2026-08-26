class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        column = len(grid[0])
        vis = [[False for _ in range(column)] for _ in range(rows)]
        maxArea = 0
        
        def dfs(i,j):
            if i<0 or j<0 or i>=rows or j>=column or vis[i][j] or grid[i][j] != 1:
                return 0
            vis[i][j] = True
            return (1 + dfs(i-1,j) + dfs(i+1,j) + dfs(i,j-1) + dfs(i,j+1))
        for i in range(rows):
            for j in range(column):
                if grid[i][j] ==1 and not vis[i][j]:
                    maxArea = max(dfs(i,j),maxArea)            
        return maxArea  