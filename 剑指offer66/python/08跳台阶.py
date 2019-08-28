# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        res = [1, 2]
        if number < 2: return res[number-1]
        for i in range(2, number):
            res.append(res[i - 1] + res[i - 2])
        return res[number-1]