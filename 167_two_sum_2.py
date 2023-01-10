class Solution:
    def twoSum(self, numbers, target):
        left,right = 0,len(numbers)-1
        
        while left< right:
            if numbers[left] + numbers[right] > target: right -=1
            elif numbers[left] + numbers[right] < target: left +=1
            else: return [left +1,right+1]        
        
numbers = [2,7,11,15]
target = 9        
obj =  Solution()
print(obj.twoSum(numbers,target))