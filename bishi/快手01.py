def huitui(s):
    string = s.split(";")
    print(string)
    if len(string) < 2: return "没有输入字符"
    qiegefu = string[0]
    str_in = string[1]
    stack = []
    print(str_in)
    for c in str_in:
        if c != qiegefu:
            stack.append(c)
        else:
            if stack:
                stack.pop()
    print("".join(stack))


s = "Y;ABYYYYYYCYDDY"
huitui(s)