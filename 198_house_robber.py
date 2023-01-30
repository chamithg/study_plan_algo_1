class Solution:
    def rob(self, nums):
        rob1, rob2 = 0, 0
        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            # this will figure out the max loot can be collected at each point of the time
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
            
nums = [2,7,9,3,1]
obj = Solution()
print(obj.rob(nums))