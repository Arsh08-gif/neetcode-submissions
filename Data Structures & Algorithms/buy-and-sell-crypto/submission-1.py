class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        
        # Approach 1
        # for i in range(n):
        #     j = i+1
        #     while(j<n):
        #         profit = prices[j] - prices[i]
        #         max_profit = max(max_profit, profit)
        #         j+=1

        # Approach 2
        buy_price = prices[0]
        for i in range(1,n):
            profit = prices[i] - buy_price
            max_profit = max(max_profit, profit)
            if buy_price > prices[i]:
                buy_price = prices[i]
            
        return max_profit

        