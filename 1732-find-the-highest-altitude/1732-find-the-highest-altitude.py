class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_average = 0
        current_sum = max_average
        for i in range(len(gain)):
            current_sum += gain[i]
            max_average = max(current_sum, max_average)
        return max_average
        