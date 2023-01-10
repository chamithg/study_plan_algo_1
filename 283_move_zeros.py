class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonZero = len(nums)
        i = 0

        while i<nonZero:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                nonZero -=1
            else:
                i+=1
        
        return nums

nums = [0,1,0,3,12]   
obj = Solution()
print(obj.moveZeroes(nums))