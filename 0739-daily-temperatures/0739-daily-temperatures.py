class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        stack = list()
        answer = [0 for _ in range(n)]

        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                answer[idx] = i - idx
            stack.append(i)
        return answer