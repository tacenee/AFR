# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res = []
        if not matrix: return
        start = 0
        row = len(matrix)
        col = len(matrix[0])
        while row > 2 * start and col > 2 * start:
            res = self.helper(matrix, start, res)
            start += 1
        return res

    def helper(self, matrix, start, list):
        print(matrix)
        endX = len(matrix[0])-start-1
        endY = len(matrix)-start-1
        for i in range(start, len(matrix[0]) - start):
            list.append(matrix[start][i])
        for j in range(start + 1, len(matrix) - start):
            list.append(matrix[j][-1 - start])
            # print(matrix[j][-1 - start])
        print(matrix[endY][endX:start])
        print(endX,endY,start)
        for k in matrix[-1 - start][-1 - start:start]:
            print("#######")
            list.append(k)
            print(matrix[-1 - start][k])
        for m in range(len(matrix) - 2 - start, -1 + start):
            print(matrix[m][start])
            list.append(matrix[m][start])
        return list


print(Solution().printMatrix([[1, 2], [3, 4]]))
