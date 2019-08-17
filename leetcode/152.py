class Solution:
    def maxProduct(self, nums) -> int:
        ret, imax, imin = float('-inf'), 1, 1
        for num in nums:
            if num < 0:
                imax, imin = imin, imax
            imax = max(imax * num, num)
            imin = min(imin * num, num)
            ret = max(ret, imax)
        return ret

        # if not nums: return
        # res = nums[0]
        # pre_max = nums[0]
        # pre_min = nums[0]
        # for num in nums[1:]:
        #     cur_max = max(pre_max * num, pre_min * num, num)
        #     cur_min = min(pre_max * num, pre_min * num, num)
        #     res = max(res, cur_max)
        #     pre_max = cur_max
        #     pre_min = cur_min
        # return res

