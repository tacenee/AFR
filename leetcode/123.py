def maxProfit(prices):
    #下面注释的方法有点点问题，还没找出具体错在哪里
    # dp_not, dp_in = 0, float('-inf')
    # dp_pre = 0
    # for i in range(len(prices)):
    #     temp = dp_not
    #     print(i, dp_not, dp_in + prices[i])
    #     dp_not = max(dp_not, dp_in + prices[i])
    #     print(dp_pre)
    #     dp_in = max(dp_in, dp_pre - prices[i])
    #     print(dp_not, dp_in)
    #     dp_pre = temp
    # return dp_not

    if not prices: return 0
    n = len(prices)
    dp = [[0] * n for _ in range(3)]
    for k in range(1, 3):
        pre_max = -prices[0]
        for i in range(1, n):
            pre_max = max(pre_max, dp[k - 1][i - 1] - prices[i])
            dp[k][i] = max(dp[k][i - 1], prices[i] + pre_max)
    return dp[-1][-1]


prices = [2, 1, 2, 0, 1]
re = maxProfit(prices)
print(re)
