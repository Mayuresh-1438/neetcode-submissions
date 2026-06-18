class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        op = []
        prefix = []
        multi = 1
        for i in nums:
            prefix.append(multi)
            multi *= i
        suffix = []
        n = 1
        for i in nums[::-1]:
            suffix.insert(0,n)
            n *= i
        for i in range(len(nums)):
            op.append(prefix[i]*suffix[i])
        return op