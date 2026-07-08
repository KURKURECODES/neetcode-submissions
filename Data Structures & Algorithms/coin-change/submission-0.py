class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for i in range(amount):
            for c in coins:
                if(i+c<=amount):
                  dp[i+c]=min(dp[i+c],dp[i]+1)
        if(dp[amount]==float('inf')):
            return -1
        return dp[amount]
        

        