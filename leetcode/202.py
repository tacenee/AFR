class Solution:
    def isHappy(self, n: int) -> bool:
        if not n: return False
        new_int = str(n)
        res = 0
        # 用set查询比数组快很多
        visit = set()
        while res != 1:
            if new_int in visit: return False
            res = 0
            for num in new_int:
                res += int(num) * int(num)
            visit.add(new_int)
            new_int = str(res)
        return True


print(Solution().isHappy(19))
