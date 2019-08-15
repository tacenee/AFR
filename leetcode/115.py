class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        sl = len(s)
        tl = len(t)
        dp = [[0] * (sl + 1) for _ in range(tl + 1)]
        for i in range(sl + 1):
            dp[0][i] = 1
        for i in range(1, tl + 1):
            for j in range(1, sl + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]
