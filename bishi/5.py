#腾讯8.17笔试第五题
def xiuxi(pre_day, g, j, day):
    if day >= len(g): return 0
    if not pre_day:
        if not g[day] and not j[day]:
            return xiuxi(pre_day, g, j, day + 1) + 1
        else:
            return min(xiuxi(not pre_day, g, j, day + 1), xiuxi(pre_day, g, j, day + 1) + 1)
    else:
        return xiuxi(not pre_day, g, j, day + 1) + 1


pre_day = False
g = [1, 1, 0, 0]
j = [0, 1, 1, 0]
print(xiuxi(pre_day, g, j, 0))
