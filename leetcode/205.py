class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        return self.half(s, t) and self.half(t, s)

    def half(self, s, t):
        ret = {}
        for i in range(len(s)):
            if s[i] not in ret:
                ret[s[i]] = t[i]
            elif ret[s[i]] != t[i]:
                return False
        return True