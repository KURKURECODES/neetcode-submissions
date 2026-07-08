class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if abs(target) > total:
            return 0

        if (target + total) % 2:
            return 0

        req = (target + total) // 2

        dp = [0] * (req + 1)
        dp[0] = 1

        for num in nums:
            for s in range(req, num - 1, -1):
                dp[s] += dp[s - num]

        return dp[req]