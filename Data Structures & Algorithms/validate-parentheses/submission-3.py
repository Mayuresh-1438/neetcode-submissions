class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")":"(","]":"[","}":"{"}
        stack = []
        for ch in s:
            if ch not in pairs:
                stack.append(ch)
            elif (len(stack)>0 and stack.pop() == pairs[ch]):
                continue
            else: 
                return False
        return len(stack) == 0