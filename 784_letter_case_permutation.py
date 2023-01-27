class Solution:
    def letterCasePermutation(self, s):
        output = [""]
        for c in s:
            tmp = []
            if c.isalpha():
                for o in output:
                    tmp.append(o+c. lower())
                    tmp.append(o+c.upper())
            else:
                for o in output:
                    tmp.append(o+c)
            output = tmp
            
        return output
        
        
        


s = "a1b2"
obj = Solution()
print(obj.letterCasePermutation(s))