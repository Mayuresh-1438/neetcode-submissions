class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {')':'(','}':'{',']':'['}
        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if not stack or stack[-1] != mp[i]:
                    return False
                stack.pop()
        return not stack