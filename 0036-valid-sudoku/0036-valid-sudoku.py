class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [list() for _ in range(9)]
        columns = [list() for _ in range(9)]
        boxes = [list() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    rows[i].append(element)
                    columns[j].append(element)
                    boxes[(i//3)*3+j//3].append(element)

        for row, column, box in zip(rows, columns, boxes):
            if len(row) != len(set(row)) or len(column) != len(set(column)) or len(box) != len(set(box)) :
                return False
        return True