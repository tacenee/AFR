class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not len(nums):return 0
        res = float('inf')
        cur = 0
        left = 0
        for right in range(len(nums)):
            cur += nums[right]
            while cur >= s:
                res = min(res, right - left + 1)
                cur -= nums[left]
                left += 1
        return res if res != float('inf') else 0 




print(Solution().minSubArrayLen(11, [1, 2, 3, 4, 5]))
