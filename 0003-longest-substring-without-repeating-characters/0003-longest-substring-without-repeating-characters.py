class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        r = 0
        l = 0
        max_len = 0
        seen_char = {}
        while r<len(s) and l<len(s):
            curr_char = s[r]
            if curr_char in seen_char:
                prev_ = seen_char[curr_char]
                l = max(l,prev_+1)
            seen_char[curr_char] = r
            max_len = max(max_len,r-l+1)
            r+=1
        return max_len 
        