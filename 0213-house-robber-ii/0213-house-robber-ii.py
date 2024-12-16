class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp1 = [0 for _ in range(n)]
        dp2 = [0 for _ in range(n)]

        dp1[0] = nums[0]
        if n >= 2 :
            dp1[1] = nums[0]
        for i in range(2, n-1):
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i])

        dp2[0] = 0
        if n >= 2 :
            dp2[1] = nums[1]
        for i in range(2, n):
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i])

        if n >= 2 :
            return max(dp1[-2], dp2[-1])
        else:
            return nums[0]