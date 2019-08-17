class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        #         negativerFlag = numerator * denominator <0
        #         numerator = abs(numerator)
        #         denominator = abs(numerator)
        #         numList = []
        #         cnt = 0
        #         loopDict = []
        #         loopStr  = None
        #         # ret = ""
        #         # first = numerator // denoinator
        #         # lat = numerator % denoinator
        #         # ret.append("{}.".format(first))
        #         while True:
        #             # num = lat*10 // denoinator
        #             # ret.append(num)
        #             # lat = lat*10 % denoinator
        #             numList.append(str(numerator // denominator))
        #             cnt += 1
        #             numerator = 10 * (numerator % denominator)
        #             if numerator == 0:
        #                 break
        #             loc = loopDict.get(numerator)
        #             if loc:
        #                 loopStr = ''.join(numList[loc:cnt])
        #                 break
        #             loopDict[numerator] = cnt

        #         ans = numList[0]

        #         if len(numList) > 1:
        #             ans += '.'

        #         if loopStr:
        #             ans += "".join(numList[1:len(numList)-len(loopStr)]) + "(" + loopStr + ")"
        #         else:
        #             ans += "".join(numList[1:])

        #         if negativerFlag:
        #             ans = '-' + ans
        #         return ans
        sign = False  # <0
        if (numerator < 0 and denominator < 0) or (numerator > 0 and denominator > 0):
            sign = True
        child = abs(numerator)
        parent = abs(denominator)
        result = []
        sh = child // parent
        yu = child % parent
        if yu == 0:
            return str(sh) if sign else str(-1 * sh)
        result.append(str(sh))
        result.append(".")
        record = []
        while True:
            #有三种情况
            #余数为0说明除完了
            if yu == 0:
                break
            #余数不在record里面，说明还没有循环
            elif yu not in record:
                record.append(yu)
                temp = yu * 10
                result.append(str(temp // parent))
                yu = temp % parent
            else:
                #余数在record里面说明开始了循环
                index = record.index(yu)
                #结果为循环开始前面的字串+（循环的字串）
                result = result[:2 + index] + ['('] + result[2 + index:] + [')']
                break
        #如果有符号，加上符号位
        return ''.join(result) if sign else "-" + ''.join(result)
