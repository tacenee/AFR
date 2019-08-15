# def charu(nums):
#
#     for i in range(len(nums) - 1):
#         right = i
#         for j in reversed(range(right)):
#             if nums[j] > nums[right]:
#                 nums[j], nums[right] = nums[right], nums[j]
#             else:
#                 break
#     return nums

def charu(nums):
    for i in range(len(nums) - 1):
        right = i + 1
        for j in reversed(range(0, right)):
            print(j)
            if nums[j] > nums[right]:
                nums[j], nums[right] = nums[right], nums[j]
            else:
                break
    return nums


if __name__ == '__main__':
    nums = [111, 3, 8, 5, 6, 7, 2, 9, 16, 12, 14]
    print(charu(nums))
