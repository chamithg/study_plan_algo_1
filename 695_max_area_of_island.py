class Solution:
    def maxAreaOfIsland(self, grid) :
        maxArr = 0
        height = len(grid)
        width = len(grid[0])
        
        
        def dfs(r,c):
            grid[r][c] = "x"
            top, left, botom, right = 0,0,0,0
            if r> 0 and grid[r-1][c] == 1:
                top = dfs(r-1,c)
            if c > 0 and grid[r][c-1] == 1:
                left = dfs(r,c-1)
            if r < height-1 and grid[r+1][c] == 1:
                botom = dfs(r+1,c)
            if c < width-1 and grid[r][c+1] == 1:
                right = dfs(r,c+1)
            return 1+top + botom+left+right
        
        for r in range(height):
            for c in range(width):
                if grid[r][c] == 1:
                    tempArr = dfs(r,c)
                    maxArr = max(tempArr,maxArr)
        
        
        return maxArr
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
obj = Solution()
print(obj.maxAreaOfIsland(grid))