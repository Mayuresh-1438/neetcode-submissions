class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        comb = []
        ans = []
        candidates.sort()
        def combination(i,target):
            if target == 0:
                ans.append(comb.copy())
                return
            if i == len(candidates) or target < 0:
                return
            comb.append(candidates[i])
            combination(i+1,target - candidates[i])
            comb.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i +=1
            combination(i+1,target)
        combination(0,target)
        return ans