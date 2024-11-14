class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        start = 1
        end = max(piles)

        while start <= end:
            mid = (start + end)//2
            result = sum([-(-pile//mid) for pile in piles])
            if result > h:
                start = mid + 1
            else:
                end = mid - 1
        
        if result > h:
            return mid + 1
        else:
            return mid
