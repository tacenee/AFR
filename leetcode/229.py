class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums)<3:return set(nums)
        t = len(nums) // 3
        m = {}
        res = set()
        for num in nums:
            if num not in m:
                m[num] = 1
            else:
                m[num] += 1
                if m[num] > t:
                    res.add(num)
        return res