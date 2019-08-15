# def guibing(nums):
#     if len(nums) < 2:
#         return nums
#     mid = len(nums) // 2
#     left = guibing(nums[:mid])
#     right = guibing(nums[mid:])
#     return gui_sort(left, right)
#
# def gui_sort(left, right):
#     ret = []
#     while left and right:
#         if left[0] < right[0]:
#             ret.append(left.pop(0))
#         else:
#             ret.append(right.pop(0))
#     if left:
#         ret += left
#     if right:
#         ret += right
#     return ret

def guibing(left, right):
    ret = []
    while left and right:
        if left[0] < right[0]:
            ret.append(left.pop(0))
        else:
            ret.append(right.pop(0))
    if left:
        ret += left
    if right:
        ret += right

    return ret


def helper(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    left = helper(nums[:mid])
    right = helper(nums[mid:])
    return guibing(left, right)


if __name__ == '__main__':
    nums = [1,4,2,5,6,3,9,8]
    ret = helper(nums)
    print(ret)