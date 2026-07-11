from functools import cache
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def dp(i, holding):
            if i >= n:
                return 0

            if holding == 0:
                return max(
                    dp(i + 1, 0),                  # Skip
                    -prices[i] + dp(i + 1, 1)     # Buy
                )
            else:
                return max(
                    dp(i + 1, 1),                  # Hold
                    prices[i] + dp(i + 2, 0)      # Sell + cooldown
                )

        return dp(0, 0)