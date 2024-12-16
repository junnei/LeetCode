class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]

        for r in range(1, n):
            for l in range(r):
                if nums[l] < nums[r]:
                    dp[r] = max(dp[r], 1 + dp[l])
                    
        return max(dp)