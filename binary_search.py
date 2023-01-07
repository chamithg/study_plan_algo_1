class Solution:
    def search(self, nums: list, target):
        
        left = 0
        right = len(nums)-1
        if target > nums[right] or target < nums[left]:return -1
        if left == right:
            if target not in nums:
                return -1
            else:
                return left
        while right >= left :
            midPoint = (left + right)//2  
            if nums[midPoint]  == target: return midPoint 
            if target > nums[midPoint]:
                left = midPoint+1
            elif target < nums[midPoint]:
                right = midPoint-1
        
        return -1

nums = [-1,0,3,5,9,12]
target = 9

obj = Solution()
print(obj.search(nums,target))