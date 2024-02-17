class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        map = {}
        for i in range(len(arr)):
            if arr[i] in map:
                map[arr[i]]+=1
            else:
                map[arr[i]]=1
        s = set()
        for value in map.values():
            if value in s:
                return False
            else:
                s.add(value)
        return True
        