def change(str1, str2):
    len1 = len(str1)  # 列
    len2 = len(str2)  # 行
    #
    # m = [[0] * (len1 + 1) for _ in range(len2 + 1)]
    # for i in range(1, len1 + 1):
    #     m[0][i] = i
    # for j in range(1, len2 + 1):
    #     m[j][0] = j
    # cos = 0
    # for i in range(1, len2 + 1):
    #     for j in range(1, len1 + 1):
    #         if str1[j - 1] == str2[i - 1]:
    #             cos = 0
    #         else:
    #             cos = 1
    #         change_dis = m[j - 1][i - 1] + cos
    #         add_dis = m[j - 1][i] + 1
    #         del_dis = m[j][i - 1] + 1
    #         m[j][i] = min(change_dis, add_dis, del_dis)
    #         print(m)
    # # print(m[len2][len1])

    m = [[i + j for j in range(len2 + 1)] for i in range(len1 + 1)]
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:
                cos = 0
            else:
                cos = 1
            change_dis = m[i - 1][j - 1] + cos
            add_dis = m[i - 1][j] + 1
            del_dis = m[i][j - 1] + 1
            m[i][j] = min(change_dis, add_dis, del_dis)
            print(m)
    print(m[len1][len2])
string = input().split(',')
change(string[0],string[1])
