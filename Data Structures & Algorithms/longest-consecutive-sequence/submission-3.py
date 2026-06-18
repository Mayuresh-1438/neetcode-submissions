class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hasSet = set(nums)
        length = 1
        max_length = 0
        if nums == []:
            return max_length
        for num in hasSet:
             if num -1 not in hasSet:
                current = num
                length = 1
                while current +1 in hasSet:
                    current += 1
                    length +=1
                if max_length < length:
                    max_length = length
        return max_length