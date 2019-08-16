def candy(ratings) -> int:
    n = len(ratings)
    left = [1 for _ in range(n)]
    right = left[:]
    for j in range(1, n):
        if ratings[j] > ratings[j - 1]: left[j] = left[j - 1] + 1
    # 边界值情况不要漏掉了
    count = left[-1]
    for k in range(n - 2, -1, -1):
        if ratings[k] > ratings[k + 1]: right[k] = right[k + 1] + 1
        # 考虑好边界值情况
        count += max(left[k], right[k])
    return count


nums = [1, 0, 2]
print(candy(nums))
