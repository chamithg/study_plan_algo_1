class Solution:
    def checkInclusion(self, s1, s2):
        
        # function to crate the counter object for strings
        def counter(st):
            charMap = {}
            for i in st:
                if i in  charMap:
                    charMap[i] +=1
                else:
                    charMap[i] = 1
            return charMap       
        # if the length is equla, compare objects   
        if len(s1) == len(s2):
            return counter(s1)== counter(s2)
            # return sorted(counter(s1).items())== sorted(counter(s1).items())
        
        # set the sliding window width to the length of the s1
        left, right = 0 ,len(s1)
        # create a hashmap of the characters of s1
        
        strMap = counter(s1)
        print(strMap)
        
        # slide the window
        while right < len(s2):
            print(s2[left])
            if s2[left] in strMap:
                
                if counter(s2[left:right]) == strMap: return True
            left+=1
            right+=1
        
        return False
        
        
s1 = "ab"
s2 = "dbass"
obj = Solution()
print(obj.checkInclusion(s1,s2))