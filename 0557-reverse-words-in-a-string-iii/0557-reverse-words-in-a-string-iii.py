class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        string = s.split(" ")
        for i in range(len(string)):
            reversed_word = string[i][::-1]
            result+=" "+reversed_word
        return result.strip()
        