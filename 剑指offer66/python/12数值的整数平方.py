# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0:return False
        if exponent == 0:return 1
        flag = False
        if base < 0: flag = True
        b, r = abs(base), abs(base)
        e = abs(exponent)
        for i in range(1, e):
            r *= b
        if flag:
            if exponent % 2 != 0:
                r = -r
        if exponent<0:
            r = 1/r
        return r
