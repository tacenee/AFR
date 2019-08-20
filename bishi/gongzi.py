#8.19商汤科技 笔试题 工资
def gongzi(n, a, b, c, f):
    # 10 0 0 0 100
    def helper(n):
        if n == 0:
            return f
        if n < 0:
            return 0
        return a * helper(n - 1) + b * helper(n - 2) + c * helper(n - 3) + 2 * n * n - n + 32767

    return helper(n)


nums = [int(num) for num in input().split()]
print(gongzi(nums[0], nums[1], nums[2], nums[3], nums[4]))
