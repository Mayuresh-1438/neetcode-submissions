class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def per(i):
            if i == len(nums):
                ans.append(nums.copy())
                return
            for j in range(i,len(nums)):
                nums[j],nums[i] = nums[i],nums[j]
                per(i+1)
                nums[j],nums[i] = nums[i],nums[j]

        per(0)
        return ans