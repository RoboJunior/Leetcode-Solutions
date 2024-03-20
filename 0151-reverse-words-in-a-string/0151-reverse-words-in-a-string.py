class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        reversed_str = ""
        for i in range(len(s)-1,-1,-1):
            reversed_str += s[i] + " "
        return reversed_str.strip()