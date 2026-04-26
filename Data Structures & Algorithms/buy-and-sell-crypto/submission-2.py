class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        profit=0
        min_=prices[0]

        for i in range(len(prices)):
            min_ = min(min_, prices[i])
            profit = max(profit, prices[i]-min_)
                
        return profit