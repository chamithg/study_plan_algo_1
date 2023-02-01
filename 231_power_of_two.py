class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n ==1:return True
        while n >2:
            n = n/2
        return n==2
        
obj = Solution()
print(obj.isPowerOfTwo(5))