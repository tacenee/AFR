def tzfe(positon, one, two, three, four):
    game_map = [[0] * 4 for _ in range(4)]
    game_map[0] = one
    game_map[1] = two
    game_map[2] = three
    game_map[3] = four

    def helper(postion, g_map):
        res = [[0] * 4 for _ in range(4)]
        if postion == 1:  # 向上
            for i in range(4):
                row = 0
                index = 0
                # 每一列从上往下
                while row < 3:
                    print(row, res[i])
                    if g_map[row][i] == g_map[row + 1][i] and game_map[row][i] != 0:
                        res[index][i] = g_map[row][i] * 2
                        row += 2
                        index += 1
                    elif game_map[row][i] == 0:
                        row += 1
                    else:
                        res[index][i] = g_map[row][i]
                        row += 1
                        index += 1

        elif postion == 2:  # 向下
            for i in range(4):
                row = 3
                index = 3
                # 每一列从下往上
                while row > 0:
                    if g_map[row][i] == g_map[row - 1][i] and g_map[row][i] != 0:
                        res[index][i] = g_map[row][i] * 2
                        row -= 2
                        index -= 1
                    elif g_map[row][i] == 0:
                        row -= 1
                    else:
                        res[index][i] = g_map[row][i]
                        row -= 1
                        index -= 1

        elif postion == 3:  # 向左
            for i in range(4):
                col = 3
                index = 3
                # 每行 从右往左
                while col > 0:
                    if g_map[i][col] == g_map[i][col - 1] and g_map[i][col] != 0:
                        res[i][index] = g_map[i][col] * 2
                        col -= 2
                        index -= 1
                    elif g_map[i][col] == 0:
                        col -= 1
                    else:
                        res[i][index] = g_map[i][col]
                        col -= 1
                        index -= 1

        elif postion == 4:  # 向右
            for i in range(4):
                col = 0
                index = 0
                # 每行从左到右
                while col > 0:
                    if g_map[i][col] == g_map[i][col + 1] and g_map[i][col] != 0:
                        res[i][index] = g_map[i][col] * 2
                        col += 2
                        index += 1
                    elif g_map[i][col] == 0:
                        col += 1
                    else:
                        res[i][index] = g_map[i][col]
                        col += 1
                        index += 1

        return res

    res = helper(positon, game_map)
    for row in res:
        print(" ".join(str(num) for num in row))


positon = 1
one = [int(num) for num in "0 0 0 2".split()]
two = [int(num) for num in "0 0 0 2".split()]
three = [int(num) for num in "0 0 4 8".split()]
four = [int(num) for num in "0 0 4 8".split()]
tzfe(positon, one, two, three, four)
