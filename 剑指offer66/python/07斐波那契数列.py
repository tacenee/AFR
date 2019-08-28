# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        # if n == 0: return 0
        # if n == 1: return 1
        # return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)
        res = [0, 1]
        if n < 2: return res[n]
        for i in range(2, n + 1):
            res.append(res[i - 1] + res[i - 2])
        return res[n]


print(Solution().Fibonacci(30))
