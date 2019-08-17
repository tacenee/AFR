#冒泡排序也是可疑的 都是利用x + y > y + x，确定最小的值
class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num

        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if int(str(nums[i]) + str(nums[j])) < int(str(nums[j]) + str(nums[i])):
        #             nums[i], nums[j] = nums[j], nums[i]
        # return "0" if nums[0] == 0 else ''.join(str(i) for i in nums)


