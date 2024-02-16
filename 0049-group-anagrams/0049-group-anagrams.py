class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answers = []
        hashmap = {}
        for i in range(len(strs)):
            hashed = "".join(sorted(strs[i]))
            if hashed in hashmap:
                hashmap[hashed].append(strs[i])
            else:
                hashmap[hashed] = [strs[i]]
        for i in hashmap.values():
            answers.append(i)
        return answers
        