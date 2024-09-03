from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hash_map = Counter(nums)
        
        def custom_sort(n):
            return (hash_map[n], -n)
        
        nums.sort(key=custom_sort)
        
        return nums
        