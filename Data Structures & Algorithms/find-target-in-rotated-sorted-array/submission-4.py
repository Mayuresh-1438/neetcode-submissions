class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <r :
            mid = (l +r)//2
            if nums[r] < nums[mid]:
                l = mid + 1 
            else:
                r = mid
        pivot = l

        def bs(left: int, right: int) -> int:
            while left <= right:
                mid =  (left + right)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        if nums[pivot] <= target <= nums[-1]:
            return bs(pivot, len(nums)-1)
        else:
            return bs(0, pivot-1)