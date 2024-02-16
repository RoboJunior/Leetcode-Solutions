class Solution:
    def solution(self,digits,digit_to_string,ans,permutation,index):
        if len(permutation) == len(digits):
            ans.append(permutation)
            return
        current_digit = digits[index]
        current_str = digit_to_string[current_digit]
        for i in range(len(current_str)):
            char = current_str[i]
            self.solution(digits,digit_to_string,ans,permutation+char,index+1)
        
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        if len(digits) == 0:
            return []
        digit_to_string = {
            "2": "abc",
            "3": "def",
            "4": "ghi",  
            "5": "jkl",  
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            }
        self.solution(digits,digit_to_string,ans,"",0)
        return ans
        