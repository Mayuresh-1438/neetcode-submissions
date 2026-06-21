class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            buy = i
            sell = i+1
            while sell < len(prices):
                max_profit = max(max_profit, prices[sell]-prices[buy])
                sell +=1
        return max_profit