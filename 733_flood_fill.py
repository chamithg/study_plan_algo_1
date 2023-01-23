class Solution:
    def floodFill(self, image, sr, sc, color):
        height = len(image)
        width = len(image[0])
        defCol = image[sr][sc]
        
        def fill(r,c):
            if image[r][c]== defCol:
                image[r][c] == color
            
            
        
                    
                
        

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2  
obj = Solution()
print(obj.floodFill(image,sr,sc,color))