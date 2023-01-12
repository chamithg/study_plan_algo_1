class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        left,right = 0,len(s)-1
        
        while left <right:
            temp = s[left]
            s[left]=s[right]
            s[right]= temp
            left +=1
            right -=1
            
        return s
        

s = ["h","e","l","l","o"]
obj = Solution()
print(obj.reverseString(s))