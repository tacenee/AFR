class Solution:
    def rob(self, nums) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        def helper(nums):
            last, now = 0, 0
            for num in nums:
                last, now = now, max(last + num, now)
            return now
        return max(helper(nums[1:]),helper(nums[:-1]))