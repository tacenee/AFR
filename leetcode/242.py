class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ret = {}
        for i in range(len(s)):
            if s[i] not in ret:
                ret[s[i]] = 1
            else:
                ret[s[i]] += 1
        for i in range(len(s)):
            if t[i] not in ret:
                return False
            else:
                ret[t[i]] -= 1
                # 把用完的数字pop出去，保证每个字母数量一致
                if ret[t[i]] == 0:
                    ret.pop(t[i])
        return True