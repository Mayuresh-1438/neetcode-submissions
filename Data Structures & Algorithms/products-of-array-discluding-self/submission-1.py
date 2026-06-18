class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        for i in range(len(nums)):
            multi = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                multi *= nums[j]
            prefix.append(multi)
        return prefix