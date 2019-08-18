class Solution:
    def rob(self, nums) -> int:
        last, now = 0, 0
        for num in nums:
            last, now = now, max(last + num, now)
        return now