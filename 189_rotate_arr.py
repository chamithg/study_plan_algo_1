class Solution:
    def rotate(self, nums,k) :
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #  solution 1 --> works but poor time and memory complexity
        for i in range(k):
            temp = nums[-1]
            del nums[-1]
            nums.insert(0,temp)
            
        return nums
nums = [1,2,3,4,5,6,7]
k = 3
obj = Solution()
print(obj.rotate(nums,k))