import sys
def yansuo(s):
    if not s:return s
    res = ""
    str_len = len(s)
    if str_len == 1:
        return s
    s += '#'
    for i in range(1, str_len+1):
        if s[i] != s[i - 1]:
            res += s[i - 1]
    sys.stdout.write(res)
string = sys.stdin.readline()
yansuo(string)



