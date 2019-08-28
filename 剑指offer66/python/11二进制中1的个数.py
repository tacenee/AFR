# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        # 把一个整数和它减去1的结果做位与运算，相当于把它最右边的1变成0。
        return sum([(n >> i & 1) for i in range(0, 32)])
