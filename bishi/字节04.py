def maxyueshu(n, nums):
    r_map = {}

    def helper(num1, num2):
        if num1 < num2:
            num1, num2 = num2, num1
        while num1 % num2 != 0:
            num1, num2 = num2, num1 % num2
        return num2

    for i in range(n - 1):
        for j in range(i + 1, n):
            t = helper(nums[i], nums[j])
            if t != 1:
                if nums[i] not in r_map:
                    r_map[nums[i]] = []
                    r_map[nums[i]].append(nums[j])
                else:
                    if nums[j] not in r_map[nums[i]]:
                        r_map[nums[i]].append(nums[j])
                if nums[j] not in r_map:
                    r_map[nums[j]] = []
                    r_map[nums[j]].append(nums[j])
                else:
                    if nums[i] not in r_map[nums[j]]:
                        r_map[nums[j]].append(nums[i])
    # print(r_map)
    count = float("-inf")
    for m in r_map:
        count = max(len(r_map[m]), count)
    # print(r_map)
    # print(max(r_map.values()))
    print(count + 1)


n = int(input())
nums = [int(num) for num in input().split()]
maxyueshu(n, nums)
