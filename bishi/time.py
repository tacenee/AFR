import time
def time_change(day):
    cur = int(time.time())
    print(cur)
    one_sec = 60*60*24
    day_sec = int(day) * 60 * 60 * 24
    ret = cur + day_sec

    tian = ret // one_sec

    # 1970年1月1日0点 -- 0 1972闰年
    four_nian = tian / (365*3 + 366)
    yu_day = tian % (365*3 + 366)

    yu_nian = 0
    t = yu_day // 365
    if yu_day > 365:
        yu_nian += t
    #如果余数小于365天，因为第一年闰年
    runnian = True if t < 1 else False
    yue_map = [31,28,31,30,31,30,31,31,30,31,31,30]
    if runnian:
        yue_map[1] = 29
    ret_yue = 1
    for i in range(len(yue_map)):
        if yu_day > yue_map[i]:
            yu_day -= yue_map[i]
            ret_yue += 1
        else:
            break

    ret_nian = 1970 + four_nian * 4 + yu_nian
    print("{}年{}月{}日".format(ret_nian,ret_yue,yu_day))

time_change(1)