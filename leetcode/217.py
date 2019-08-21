class Solution:
    def containsDuplicate(self, nums) -> bool:
        ret = {}
        for i in range(len(nums)):
            if nums[i] not in ret:
                ret[nums[i]] = True
            elif ret[nums[i]]:
                return True
        return False