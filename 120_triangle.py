class Solution:
    def minimumTotal(self, triangle):
        total =0
        found_ind = 0
        
        for i in triangle:
            if len(i) == 1: total += i[0]
            else:
                total += min(i[found_ind],i[found_ind+1])
                if i[found_ind] > i[found_ind+1]:
                    found_ind = found_ind+1
                    

        return total
# triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
triangle = [[-1],[2,3],[1,-1,-3]]
obj = Solution()
print(obj.minimumTotal(triangle))