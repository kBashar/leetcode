class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        f_p = 0
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - prices[f_p])
            if prices[f_p]>prices[i]:
                f_p = i
        return profit