class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in {'+', '-', '*', '/'}:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(str(int(eval(num2 + tokens[i] + num1))))
            else:
                stack.append(tokens[i])
        return stack[-1]
