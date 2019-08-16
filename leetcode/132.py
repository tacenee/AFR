def minCut(self, s: str) -> int:
    #回溯方法会超时
    # if s == s[::-1]:return 0
    # ans = float("inf")
    # #ans为当前字串最小分割数
    # for i in range(1, len(s) + 1):
    #     if s[:i] == s[:i][::-1]:
    #         ans = min(self.minCut(s[i:]) + 1, ans)
    # return ans

