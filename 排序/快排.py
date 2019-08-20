# def pitation(arr, left, right):
#     pivat = arr[left]
#     i = left + 1
#     index = i
#     while i <= right:
#         if arr[i] < pivat:
#             arr[index], arr[i] = arr[i], arr[index]
#             index += 1
#         i += 1
#     arr[left], arr[index - 1] = arr[index - 1], arr[left]
#     return index - 1
#
#
# def kuaipai(arr, left, right):
#     if left < right:
#         pi = pitation(arr, left, right)
#         kuaipai(arr, left, pi - 1)
#         kuaipai(arr, pi + 1, right)


def pitation(nums, left, right):
    pivat = nums[left]
    cur, index = left + 1, left + 1
    while index <= right:
        if nums[index] < pivat:
            nums[index], nums[cur] = nums[cur], nums[index]
            cur += 1
        index += 1
    nums[left], nums[cur - 1] = nums[cur - 1], nums[left]
    return cur - 1


def kuaipai(nums, left, right):
    if left < right:
        pivat = pitation(nums, left, right)
        kuaipai(nums, left, pivat - 1)
        kuaipai(nums, pivat + 1, right)


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
# helper(arr, 0, n - 1)
kuaipai(arr, 0, n - 1)
print("排序后的数组:")
for i in range(n):
    print("%d" % arr[i])
