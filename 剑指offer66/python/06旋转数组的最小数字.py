# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray: return
        # if rotateArray[0] <= rotateArray[-1]: return rotateArray[0]
        l, r = 0, len(rotateArray) - 1
        while l < r:
            mid = (l + r) // 2
            print(rotateArray[mid], rotateArray[l])
            if rotateArray[mid] < rotateArray[l]:
                r = mid
            elif rotateArray[mid] > rotateArray[l]:
                l = mid
            else:
                break
        print(min(rotateArray[l], rotateArray[r]))


Solution().minNumberInRotateArray([2, 3, 4, 5, 1])
