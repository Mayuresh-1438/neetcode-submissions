class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid_index = (l+r)//2
            if nums[mid_index] < target:
                l = mid_index + 1
            elif nums[mid_index] > target:
                r = mid_index - 1
            else:
                return mid_index
        return -1