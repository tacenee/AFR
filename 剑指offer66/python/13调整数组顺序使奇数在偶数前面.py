# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        # 类似于选择排序，从后往前，如果前偶后奇就调换两个数字的位置
        for i in range(len(array)):
            for j in range(i, 0, -1):
                if array[j] % 2 == 1 and array[j - 1] % 2 == 0:
                    array[j], array[j - 1] = array[j - 1], array[j]
        return array
