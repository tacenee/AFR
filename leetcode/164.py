class Solution:
    def maximumGap(self, nums) -> int:
        if len(nums) <= 1: return 0
        nums.sort()
        minValue = float(0)
        for i in range(len(nums) - 1):
            cha = nums[i + 1] - nums[i]
            minValue = max(cha, minValue)
        return minValue