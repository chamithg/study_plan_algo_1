class Solution:
    def lengthOfLongestSubstring(self, s) :
        if len(s)==1: return 1
        start = 0
        chars = {}
        strLen = 0
        
        for i,c in enumerate(s):
            # if c met before
            if c in chars and start <= chars[c]:
                start = chars[c] +1
            else:
                strLen = max(strLen, i-start+1)
            chars[c]= i
        
        return strLen

        


s = "pwwkew"
obj = Solution()
print(obj.lengthOfLongestSubstring(s))