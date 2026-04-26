class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0

        min_at_j = prices[0]
        max_prof = 0

        for z in range(1, len(prices)):
            if prices[z] - min_at_j > max_prof:
                max_prof = prices[z] - min_at_j
            else:
                min_at_j = min(min_at_j, prices[z])
        return max_prof