class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i =='+':
                op1 = stack.pop()
                op2 = stack.pop()
                result = op2 + op1
                stack.append(result)
            elif i == '-':
                op1 = stack.pop()
                op2 = stack.pop()
                result = op2 - op1
                stack.append(result)
            elif i == '*':
                op1 = stack.pop()
                op2 = stack.pop()
                result = op2 * op1
                stack.append(result)
            elif i == '/':
                op1 = stack.pop()
                op2 = stack.pop()
                result = int(op2 / op1)
                stack.append(result)
            else:
                stack.append(int(i))
        return stack[-1]