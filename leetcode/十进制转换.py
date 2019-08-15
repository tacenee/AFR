def zhuanhuan(num, n):
    jmap = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    nums = []
    while True:
        s = num // n
        y = num % n
        nums += [y]
        if not s:
            break
        num = s

    for i in nums[::-1]:
        print(jmap[i], end='')


zhuanhuan(31, 16)
