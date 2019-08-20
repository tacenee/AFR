import math

#8。19商汤科技 确定能组成完全平方的组合有多少个
def wqpf(nums):
    res = [0 for _ in range(len(nums))]
    visit = {num: [] for num in nums}
    for i in range(len(nums)):
        index = 0
        while index < len(nums):
            if i == index:
                index += 1
                continue
            if truewqpf(nums[i], nums[index]):
                if nums[index] not in visit[nums[i]]:
                    res[i] += 1
                    visit[nums[i]].append(nums[index])
            index += 1
    res.sort()
    if res[0] == 0: return 0
    return res[-1]


def truewqpf(x, y):
    sum = x + y
    gen = math.sqrt(sum)
    return True if gen * gen == sum else False


nums = [int(num) for num in input().split()]
print(wqpf(nums))
