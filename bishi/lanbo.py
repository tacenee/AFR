#8.19商汤科技 逆波兰 leetcode150原题
def evalRPN(tokens) -> int:
    stack = []
    for i in range(len(tokens)):
        if tokens[i] in {'+', '-', '*', '/'}:
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(str(int(eval(num2 + tokens[i] + num1))))
        else:
            stack.append(tokens[i])
    return stack[-1]


s = "2 1 + 3 *"
tokens = s.split()
print(evalRPN(tokens))
