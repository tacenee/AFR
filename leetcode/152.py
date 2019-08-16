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