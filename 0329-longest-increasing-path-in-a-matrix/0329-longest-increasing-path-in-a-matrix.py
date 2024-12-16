class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [
            [0 for _ in range(m)]
            for _ in range(n)
        ]

        dxys = [
            [-1, 0],
            [1, 0],
            [0, 1],
            [0, -1]
        ]

        def in_range(x, y):
            return 0<=x<n and 0<=y<m


        for x in range(n):
            for y in range(m):
                for dx, dy in dxys:
                    nx, ny = x + dx, y + dy
                    if in_range(nx, ny) and matrix[nx][ny] > matrix[x][y]:
                        dp[nx][ny] += 1
                        
        q = deque((i, j) for i in range(n) for j in range(m) if dp[i][j] == 0)
        
        result = 0
        while q:
            result += 1
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in dxys:
                    nx, ny = x + dx, y + dy
                    if in_range(nx, ny) and matrix[nx][ny] > matrix[x][y]:
                        dp[nx][ny] -= 1
                        if dp[nx][ny] == 0:
                            q.append((nx, ny))
        return result