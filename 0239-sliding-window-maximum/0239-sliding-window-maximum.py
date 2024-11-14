from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        q = deque()
        answer = list()
        for i in range(n):
            item = nums[i]
            while q and q[-1] < item:
                q.pop()
            q.append(item)

            if i-k >= 0 and q[0] <= nums[i-k]:
                q.popleft()
            answer.append(q[0])

        return answer[k-1:]