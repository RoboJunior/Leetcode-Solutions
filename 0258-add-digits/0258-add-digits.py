class Solution:
    def addDigits(self, num: int) -> int:
        total_sum = 0
        splitted_nums = [int(i) for i in str(num)]
        if len(splitted_nums) == 1:
            return num
        if len(splitted_nums)>1:
            total_sum = sum(splitted_nums)
            return self.addDigits(total_sum)
        