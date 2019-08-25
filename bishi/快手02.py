def jiangxu(s):
    if not s: return
    s_list = s.split(" ")
    s = "".join(s_list)
    s_map = {}
    for c in s:
        if c not in s_map:
            s_map[c] = 1
        else:
            s_map[c] += 1
    t = sorted(s_map.items(), key=lambda x: x[1], reverse=True)
    res = []
    for k in t:
        res.append(k[0] + ":" + str(k[1]))
    print(",".join(res))


jiangxu("abccc")
