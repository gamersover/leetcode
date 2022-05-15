from ftplib import all_errors
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def find_possible_number(board, i, j):
            all_number = set(map(str, range(1, 10)))
            for index in range(9):
                if board[index][j] != ".":
                    all_number.discard(board[index][j])
                if board[i][index] != ".":
                    all_number.discard(board[i][index])
            row = i // 3
            col = j // 3
            for m in range(row*3, (row+1)*3):
                for n in range(col*3, (col+1)*3):
                    if board[m][n] != ".":
                        all_number.discard(board[m][n])
            return all_number

        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for n in find_possible_number(board, i, j):
                            board[i][j] = n
                            if solve(board):
                                return True
                        board[i][j] = "."
                        return False
            return True

        solve = solve(board)


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

Solution().solveSudoku(board)

print(board)
