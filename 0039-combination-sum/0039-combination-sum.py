class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        n = len(candidates)
        answer = list()
        result = list()
        
        def simulate(start: int, value: int):
            if value > target:
                return

            if value == target:
                answer.append(result[:])
                return

            for i in range(start, n):
                result.append(candidates[i])
                simulate(i, value + candidates[i])
                result.pop()

        simulate(0, 0)

        return answer