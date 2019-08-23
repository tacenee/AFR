class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = '+'
        num = 0
        s += '+'
        for c in s:
            if c == '':
                continue
            elif c in '0123456789':
                num = num * 10 + int(c)
                continue
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack[-1] * num)
            elif sign == '/':
                stack.append(stack[-1] * 1.0 / num)
            sign = c
            num = 0
        return sum(stack)
