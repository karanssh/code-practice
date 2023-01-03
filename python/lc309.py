from typing import List 

class Solution:
    def maxProfit2(self, prices: List[int]) -> int:
        # State: Buying or Selling?
        # If Buy -> i + 1
        # If Sell -> i + 2

        dp = {}  # key=(i, buying) val=max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]

        return dfs(0, True)
        
    def maxProfit(self, prices: List[int]) -> int:
        ## RC ##
        ## APPROACH : DP - STATE MACHINE PATTERN ##
        ## LOGIC ##
        
        """
        1. In general dynamic programming concept, we store maxprofit found till that index in dp[i], but this problem has many states i) buy ii) sell iii) cooldown 
        
        2. if in case of multiple states, what we do in (say DP state machine pattern) is we store maximum for all the possible states i.e
            a) max profit with state = buy,      on day i
            b) max profit with state = cooldown, on day i
            c) max profit with state = sell,     on day i
        
        3. For this problem
            a) dp_buy[i] = we are buying on that day. But as per question you can only buy when previous day is cooldown. so only consider dp_cooldown[i-1] and also buying on day i, will cost you some money i.e price[i]. can be written as:
                ``` dp_buy[i] = dp_cooldown[i-1] - price[i] ```
            b) dp_cooldown[i] = we are doing nothing, so whatever you have done on previous day doesn't matter. so take maximum of all previous states
                ``` dp_cooldown[i] = max( dp_cooldown[i-1], dp_buy[i-1], dp_sell[i-1] )  ```
            c) dp_sell[i] = before selling you have to buy, so we have to get max of previous_buy value from o to i. Instead of looping 0 to i, we can simply keep a max_prev_buy variable and keep track of it. And also by selling you are getting money i.e prices[i] so add prices[i] to max_prev_buy
                dp_sell[i] = (max profit you got before by buying stocks) + ( profit by selling this stock )
                ``` dp_sell[i] = max_prev_buy + prices[i]   ```
        """
        
        if len(prices) < 2 : return 0
                
        n               = len(prices)
        dp_buy          = [0 for _ in range(n)]
        dp_cooldown     = [0 for _ in range(n)]
        dp_sell         = [0 for _ in range(n)]
        
        dp_cooldown[0]  = 0
        dp_buy[0]       = -prices[0]
        dp_sell[0]      = float('-inf')
        max_prev_buy    = dp_buy[0]
        
        for i in range(1, n):
            dp_cooldown[i]  = max( dp_cooldown[i-1], dp_buy[i-1], dp_sell[i-1] )
            dp_buy[i]       = dp_cooldown[i-1] - prices[i]
            dp_sell[i]      = max_prev_buy + prices[i]
            
            max_prev_buy    = max( max_prev_buy, dp_buy[i] )
            
        return max( dp_cooldown[-1], dp_sell[-1] )