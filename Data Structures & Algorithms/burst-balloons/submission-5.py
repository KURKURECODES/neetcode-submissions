from functools import cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        num=[1]+nums+[1]
        @cache
        def bt(l,r):
            if(l>r):
                return 0
            maxi=0
            for k in range(l,r+1):
                sol=(bt(l,k-1)+bt(k+1,r)+num[l-1]*num[k]*num[r+1])
                maxi=max(maxi,sol)
            
            return maxi
        return bt(1,len(num)-2)
