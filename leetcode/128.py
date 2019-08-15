def longestConsecutive(nums):
    # 暴力法执行时间太长了
    # ret = 0
    # for num in nums:
    #     if num - 1 not in nums:
    #         s = num + 1
    #         while s in nums:
    #             s += 1
    #         ret = max(ret, s - num)
    # return ret

    # 先排序
    if not nums:
        return 0

    nums.sort()

    longest_streak = 1
    current_streak = 1
    print(nums)
    for i in range(len(nums) - 1):
        if nums[i + 1] != nums[i]:
            if nums[i + 1] == nums[i] + 1:
                current_streak += 1
            else:
                print(i)
                longest_streak = max(current_streak, longest_streak)
                current_streak = 1
    # 最后一个也是连续的情况，没有机会计算longest_streak
    return max(current_streak, longest_streak)


nums = [100, 4, 200, 1, 3, 2]
ret = longestConsecutive(nums)
print(ret)
