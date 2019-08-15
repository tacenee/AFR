class Solution:
    def minimumTotal(self, triangle):
        # 自顶向下递归会超时
        # def back(level, index, min):
        #     if level > len(triangle):
        #         return min
        #     min += triangle[level][index]
        #     return min(back(level + 1, index, min), back(level + 1, index + 1, min))
        #
        # return back(0, 0, 0)

        #自底向上的方法可以 不会超时，思路差不多
        # if len(triangle) == 0:
        #     return 0
        # row = len(triangle) - 2
        # for row in range(row, -1, -1):
        #     for col in range(len(triangle[row])):
        #         triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
        # return triangle[0][0]

        #每一次计算所在位置最小值也可以，跟上一方法也差不多太多
        if not triangle:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]
        for i in range(1, len(triangle)):
            triangle[i][0] += triangle[i - 1][0]
            for j in range(1, len(triangle[i]) - 1):
                triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
            triangle[i][-1] += triangle[i - 1][-1]
        return min(triangle[-1])

