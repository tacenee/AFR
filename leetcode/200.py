class Solution:
    def numIslands(self, grid) -> int:
        # 11110
        # 11010
        # 11000
        # 00000
        if not grid: return 0
        res = 0
        row = len(grid)
        col = len(grid[0])
        visit = [[False for _ in range(col)] for _ in range(row)]

        def helper(x, y):
            if x > row - 1 or x < 0 or y > col - 1 or y < 0 or grid[x][y] == "0" or visit[x][y]:
                return
            else:
                visit[x][y] = True
                helper(x + 1, y)
                helper(x - 1, y)
                helper(x, y + 1)
                helper(x, y - 1)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and not visit[i][j]:
                    helper(i, j)
                    res += 1

        print(visit)
        print(res)
        # return res


# 11000
# 11000
# 00100
# 00011
grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
Solution().numIslands(grid)
