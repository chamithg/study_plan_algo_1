class Solution:
    def reverseWords(self, s: str) -> str:
        wordArr = s.split(" ")
        outArr =[]
        
        for i in wordArr:
            outWord = ""
            for j in reversed(range(len(i))):
                outWord +=i[j]
            outArr.append(outWord)
        output = " ".join(outArr)   
        return output


s = "Let's take LeetCode contest"

obj = Solution()
print(obj.reverseWords(s))