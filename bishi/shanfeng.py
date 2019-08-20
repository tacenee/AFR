#8.19商汤科技 求最长山峰
def shanfeng(n, nums):
    if n <= 3: return 0
    max_len = 0
    left = 0
    right = 1
    while right < n and left < n:
        if right < n and left < n and nums[right] > nums[left]:
            while right < n and nums[right] > nums[right - 1]:
                right += 1
            if right == n:
                break
            elif nums[right] == nums[right - 1]:
                left = right
                print(right, left)
                continue

            while right < n and nums[right] < nums[right - 1] :
                right += 1
            max_len = max(max_len, right - left)
            left = right
            right += 1
        else:
            left += 1
            right += 1
    return max_len


# n = 7
# nums = [int(num) for num in input().split()]
# nums = [3,3, 3, 4, 5, 6, 5, 3, 2]
nums = [3,3,3,3]
n = len(nums)
print(shanfeng(n, nums))
