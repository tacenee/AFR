import sys


def change(n, s):
    if s == " ":
        sys.stdout.write('0')
        return
    if n != len(s):
        sys.stdout.write('0')
        return
    nums = [0] * n
    flag = False  # 是否产生连续
    pre = False  # 前面是不是大写
    for i in range(n):
        if 65 <= ord(s[i]) <= 90:
            if pre:
                nums[i] += 1
                flag = True
            else:
                nums[i] += 2
                pre = True
        if ord(s[i]) >= 97:
            if flag:
                nums[i] += 2
                pre = False
                flag = False
            else:
                nums[i] += 1
                pre = False
    sys.stdout.write(str(sum(nums)))


# print(ord('Z'))
n = int(input())
s = input()
change(n, s)
