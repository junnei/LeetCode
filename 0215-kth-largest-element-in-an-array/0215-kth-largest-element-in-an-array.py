class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        while k != 0:
            nums, k = self.find(nums, k)
        return nums[0]

    def find(self, nums: list[int], k: int) -> tuple[list[int], int]:
        left, right, mid = list(), list(), list()
        limit = nums[0]
        for num in nums:
            if num > limit:
                right.append(num)
            elif num < limit:
                left.append(num)
            else:
                mid.append(num)
        len_right, len_mid = len(right), len(mid)
        if len_right >= k:
            return right, k
        elif len_right + len_mid >= k:
            return [limit], 0
        else:
            return left, k - len_right - len_mid