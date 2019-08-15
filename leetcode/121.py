class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret,min_price = 0,float('inf')
        for price in prices:
            min_price = min(min_price,price)
            ret = max(ret,price-min_price)
        return ret