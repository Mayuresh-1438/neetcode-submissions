class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        table = set()
        for val in nums:
            if  val not in table:
                table.add(val)
            else:
                return True
        return False