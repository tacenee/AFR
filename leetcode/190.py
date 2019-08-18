class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # bin 将数变成ob开头的2进制字符串
        # zfill 右对齐，左不够补零
        # int 将字符串 转换从base进制转换成10进制的整数
        return int(bin(n)[2:].zfill(32)[::-1], base=2)


        # res = 0
        # count = 32
        #
        # while count:
        #     res <<= 1
        #     # 取出 n 的最低位数加到 res 中
        #     res += n & 1
        #     n >>= 1
        #     count -= 1
        #
        # return int(bin(res), 2)



Solution().reverseBits()
