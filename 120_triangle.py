class Solution:
    def minimumTotal(self, triangle):
        #  the best way to approach this is to iterate from the bottom of the triangle.
        for i in reversed(range(len(triangle))):
            if i < len(triangle)-1:
                for j in range(len(triangle[i])):
                    triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1])

        return triangle[0][0]
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# triangle = [[-1],[2,3],[1,-1,-3]]
obj = Solution()
print(obj.minimumTotal(triangle))