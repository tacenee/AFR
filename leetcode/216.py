class Solution:
    def combinationSum3(self, k: int, n: int):
        # 大神的方法，我暂时还没搞懂双重剪枝的概念，先把答案记录一下
        def comb(k: int, n: int, start: int) -> list:  # 从start考虑，可以避免重复
            if k == 1:  # 终止条件
                if n < 10:
                    return [[n]]
                return []
            res = []
            for i in range(start + 1, min((n + 1) // 2, 10)):  # 当前数最多取到n的一半，避免重复，且得满足i<10
                for j in comb(k - 1, n - i, i):  # 回溯
                    res.append([i] + j)
            return res

        return comb(k, n, 0)

# Solution().combinationSum3(1,1)
