class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        for i in range(n):
            j = i+1
            while(j<n):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
                j+=1
            
        return max_profit

        