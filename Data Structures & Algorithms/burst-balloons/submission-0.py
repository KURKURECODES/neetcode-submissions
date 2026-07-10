from functools import lru_cache
from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Pad the array with 1s
        nums = [1] + nums + [1]
        n = len(nums)

        @lru_cache(None)
        def dp(left, right):
            # No balloons left in this interval
            if left > right:
                return 0

            ans = 0

            # Try every balloon as the last one to burst
            for k in range(left, right + 1):
                coins = (
                    dp(left, k - 1)
                    + dp(k + 1, right)
                    + nums[left - 1] * nums[k] * nums[right + 1]
                )
                ans = max(ans, coins)

            return ans

        # Solve for the original balloons
        return dp(1, n - 2)