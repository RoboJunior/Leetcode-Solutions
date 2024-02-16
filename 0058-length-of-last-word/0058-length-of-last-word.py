class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        i = len(s) - 1
        while s[i] == " ":i-=1
        for i in range(i+1):
            if s[i]!=" ":
                count+=1
            else:
                count=0
        return count
        