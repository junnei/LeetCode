class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        len_word = len(word)
        m, n = len(board), len(board[0])
        dxys = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ]

        visited = [
            [False for _ in range(n)]
            for _ in range(m)
        ]

        def in_range(x, y):
            return 0<=x<m and 0<=y<n

        def can_go(x, y, target):
            return in_range(x, y) and not visited[x][y] and target == board[x][y]
            
        def simulate(x, y, idx):
            if idx == len_word:
                return True

            for dx, dy in dxys:
                nx, ny = x + dx, y + dy
                if can_go(nx, ny, word[idx]):
                    visited[nx][ny] = True
                    if simulate(nx, ny, idx + 1):
                        return True
                    visited[nx][ny] = False
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if simulate(i, j, 1):
                        return True
                    visited[i][j] = False

        return False