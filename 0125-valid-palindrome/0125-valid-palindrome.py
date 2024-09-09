class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        
        while left<=right:
            left_char = s[left].lower()
            right_char = s[right].lower()
            
            if not left_char.isalnum():
                left+=1
            
            elif not right_char.isalnum():
                right -=1
            
            elif left_char!=right_char:
                return False
            
            else:
                left+=1
                right-=1
        
        return True