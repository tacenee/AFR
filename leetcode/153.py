class Solution:
    def findMin(self, nums) -> int:
        if len(nums) == 1: return nums[0]
        if nums[0] < nums[-1]: return nums[0]
        mid = len(nums) // 2
        if nums[-1] > nums[mid]:
            return self.findMin(nums[:mid + 1])
        else:
            return self.findMin(nums[mid:])
