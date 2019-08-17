class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        l = min(len(v1), len(v2))
        index = 0
        while index < l:
            if int(v1[index]) > int(v2[index]):
                return 1
            if int(v1[index]) < int(v2[index]):
                return -1
            index += 1
        #1.0 和 1.0
        if len(v1) == len(v2):
            return 0
        else:
            #1.0 和 1
            if len(v1) > len(v2):
                while index < len(v1):
                    if int(v1[index]): return 1
                    index += 1
            #1 和 1.1
            else:
                while index < len(v2):
                    if int(v2[index]): return -1
                    index += 1
            return 0


ver1 = "1.1"
ver2 = "1"
print(Solution().compareVersion(ver1, ver2))
