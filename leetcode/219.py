class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        lookup = {}
        for i,num in enumerate(nums):
            if num not in lookup:
                lookup[nums[i]] = i
            else:
                if i - lookup[num] <= k:
                    return True
                lookup[num] = i
        return False