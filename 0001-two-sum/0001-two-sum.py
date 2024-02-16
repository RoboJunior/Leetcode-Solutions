class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            point_to_find = target - nums[i]
            if (nums[i] in m):
                point_index = m[nums[i]]
                return [point_index,i]
            m[point_to_find]=i
        