class Solution:
    def sortedSquares(self, nums):
        output = []
        for i in reversed(range(len(nums))):
            output.append(nums[i]* nums[i])
        output.sort()
        return output
        
        


nums = [-4,-1,0,3,10]       
obj = Solution()
print(obj.sortedSquares(nums))