class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        comb = []
        ans = []
        def combination(i,target):
            if i == len(nums) or target < 0:
                return
            if target == 0:
                ans.append(comb.copy())
                return
            comb.append(nums[i])
            combination(i,target - nums[i])
            comb.pop()
            combination(i+1,target)
        combination(0,target)
        return ans
            