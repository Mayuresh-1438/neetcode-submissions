class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        arr = []
        def backtracking(openp,closep):
            if openp == closep == n:
                res.append("".join(arr))
                return
            if openp < n:
                arr.append("(")
                backtracking(openp +1,closep)
                arr.pop()
            if openp > closep:
                arr.append(")")
                backtracking(openp,closep+1)
                arr.pop()
        backtracking(0,0)
        return res