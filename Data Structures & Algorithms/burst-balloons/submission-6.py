class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        num=[1]+nums+[1]
        n=len(num)
        dp=[[0]*n for _ in range(n)]
        for lens in range(1,len(nums)+1):
            for l in range(1,len(num)-lens):
                r=l+lens-1
                for k in range(l,r+1):
                    dp[l][r]=max(dp[l][r],dp[l][k-1]+dp[k+1][r]+num[l-1]*num[k]*num[r+1])
        return dp[1][len(nums)]