class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ways=[0]*(amount+1)
        dp=[float('inf')]*(amount+1)
        dp[0]=1
        ways[0]=1
        
        for c in coins:
            for i in range(amount):
                if(i+c<=amount):
                    dp[i+c]=min(dp[i+c],dp[i]+1)
                    ways[i+c]+=ways[i]
        if(dp[amount]!=float('inf')):
            return ways[amount]
        return 0

    
        
        