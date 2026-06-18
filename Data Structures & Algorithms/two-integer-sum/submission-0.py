class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for index, num in enumerate(nums):
            check = target - num
            if check not in hashTable:
                hashTable[num] = index
            else:
                return [hashTable[check], index]