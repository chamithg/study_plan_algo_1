class Solution:
    def orangesRotting(self, grid):
        height = len(grid)
        width = len(grid[0])
        
        # count number of fresh oranges
        fresh_count = 0
        time = 0
        
        for r in range(height):
            for c in range(width):
                if grid[r][c] == 1: fresh_count +=1

        while fresh_count > 0:
            #  with each iteation of the while loop, collect coordinates of rotten oranges at the beggining
            prev = fresh_count
            rottens = []
            for r in range(height):
                for c in range(width):
                    if grid[r][c] ==2:
                        rottens.append((r,c))
            #  iterate over rotten list and make the adjacent oranges rotten
            for r,c in rottens:
                for i,j in [(r,c+1),(r,c-1),(r+1,c),(r-1,c)]:
                    if 0<= i< height and 0 <= j <width and grid[i][j] == 1:
                        grid[i][j] = 2
                        fresh_count-=1
            #  to find out all adjacent oranges rotten, keep the track of changes of fresh count
            # if fresh count not changed, which means rotting completed, so that break the loop.
            if prev == fresh_count: break
            time +=1
            
        if fresh_count >0:
            return -1
        else:return time
                        
grid = [[2,1,1],[0,1,1],[1,0,1]]
obj = Solution()
print(obj.orangesRotting(grid))