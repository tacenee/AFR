#腾讯8.17笔试第一题
def jieya(ans):
    left_index = 0
    right_index = 0
    shu_index = 0
    # HG[3|B[2|CA]]F
    for i in range(len(ans)):
        if ans[i] == '[':
            left_index = i
        elif ans[i] == ']':
            right_index = i
            break
        elif ans[i] == '|':
            shu_index = i
    if right_index == 0: return ans
    cur = ans[shu_index + 1:right_index] * int(ans[left_index + 1:shu_index])
    new_str = ans[:left_index] + cur + ans[right_index + 1:]
    return jieya(new_str)




ans = "HG[3|B[2|CA]]F"
print(jieya(ans))
