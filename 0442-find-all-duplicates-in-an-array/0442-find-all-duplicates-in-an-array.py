class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        map = {}
        for i in range(len(nums)):
            if nums[i] in map:
                map[nums[i]]+=1
            else:
                map[nums[i]]=1
        ans = []
        for k,v in map.items():
            if v>1:
                ans.append(k)
        return ans
            
        