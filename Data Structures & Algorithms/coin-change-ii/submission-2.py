class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ways=[0]*(amount+1)
        ways[0]=1
        
        for c in coins:
            for i in range(amount):
                if(i+c<=amount):
                    ways[i+c]+=ways[i]
        return ways[amount]
     

    
        
        