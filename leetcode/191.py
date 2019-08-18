class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 32
        res = 0
        while count:
            res += n & 1
            n >>= 1
            count -= 1
        return res