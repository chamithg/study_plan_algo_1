class Solution:
    def orangesRotting(self, grid):
        height = len(grid)
        width = len(grid[0])
        fresh_count = 0
        
        rotten_dict = {}
        
        # helper method to rot oranges
        def rotten(r,c,adj_oranges):
            if grid[r][c] == 1:
                adj_oranges.append(1)   
            grid[r][c] = "x"
            if r< height-1 and grid[r+1][c] ==1:
                rotten(r+1,c,adj_oranges)
            if r > 0 and grid[r-1][c] ==1:
                rotten(r-1,c,adj_oranges)
            if c < width-1 and grid[r][c+1] ==1:
                rotten(r,c+1,adj_oranges)
            if c > 0 and grid[r][c-1] ==1:
                rotten(r,c-1,adj_oranges)
            return 

        
        for r in range(height):
            for c in range(width):
                if grid[r][c] == 1 or grid[r][c] == "x" :
                    fresh_count += 1
                elif grid[r][c] == 2:
                    adj_oranges = []
                    rotten(r,c,adj_oranges)
                    print(adj_oranges)
        print(fresh_count)
        print(grid)
        
grid = [[2,1,1],[0,1,1],[1,0,1]]
obj = Solution()
print(obj.orangesRotting(grid))