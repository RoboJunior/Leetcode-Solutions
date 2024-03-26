class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            output.append(nums[i]*nums[i])
        return sorted(output)