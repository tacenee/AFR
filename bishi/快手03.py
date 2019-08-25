def zheheng(t):
    res = []

    def helper(tt, weizhi):
        if tt == 0: return
        # 设前面一格为True 后面一格为False
        helper(tt - 1, True)
        if weizhi:
            res.append("down")
        else:
            res.append("up")
        helper(tt - 1, False)

    helper(t, True)
    for r in res[::-1]:
        print(r)
zheheng(1)
