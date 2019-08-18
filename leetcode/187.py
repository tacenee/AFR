class Solution:
    def findRepeatedDnaSequences(self, s: str):
        if len(s) < 10: return []
        #利用set无序，但是查询快的特点，就不会超时
        ret = set()
        visit = set()
        for i in range(0,len(s)-9):
            tmp = s[i:i + 10]
            if tmp in visit:
                ret.add(tmp)
            visit.add(tmp)
        return list(ret)

print(Solution().findRepeatedDnaSequences("AAAAAAAAAAA"))
