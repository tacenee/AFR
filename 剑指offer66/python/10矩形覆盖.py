# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        res = [0, 1, 2]
        if number <= 2: return res[number]
        for i in range(3, number + 1):
            res.append(res[i - 1] + res[i - 2])
        return res[number]
