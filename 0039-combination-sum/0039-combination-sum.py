class Solution:
    def solution(self,candidates,target,ans,cur,index,sum):
        if sum == target:
            ans.append(cur[:])
        elif sum<target:
            n = len(candidates)
            for i in range(index,n):
                cur.append(candidates[i])
                self.solution(candidates,target,ans,cur,i,sum+candidates[i])
                cur.pop()
        return ans
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.solution(candidates,target,[],[],0,0)
        