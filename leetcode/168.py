# encoding=utf-8
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret, num = "", n
        while num:
            # ret += chr(num  % 26)
            ret += chr((num - 1) % 26 + ord('A'))
            # 进位问题，满26就会进位
            num = (num - 1) // 26
        return ret[::-1]
