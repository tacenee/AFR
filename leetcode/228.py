class Solution:
    def summaryRanges(self, nums):
        if not nums: return []
        index = 1
        res = []
        nums.append(nums[-1])
        print(nums)
        cur, pre = nums[0], nums[0]
        while index < len(nums):
            if nums[index] != cur + 1:
                if pre != cur:
                    res.append("{}->{}".format(pre, cur))
                else:
                    res.append("{}".format(pre))
                pre = nums[index]
            cur = nums[index]
            index += 1
        return res


print(Solution().summaryRanges([0,1,2,4,5,7]))
