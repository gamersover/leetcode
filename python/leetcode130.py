from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        def is_valid_pos(x, y, m, n):
            if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
                return True
            return False

        def find_valid_pos(x, y, m, n):
            all_pos = []
            if is_valid_pos(x-1, y, m, n):
                all_pos.append((x-1, y))
            if is_valid_pos(x+1, y, m, n):
                all_pos.append((x+1, y))
            if is_valid_pos(x, y-1, m, n):
                all_pos.append((x, y-1))
            if is_valid_pos(x, y+1, m, n):
                all_pos.append((x, y+1))
            return all_pos


        def dfs(board, x, y, m, n):
            board[x][y] = '|'
            for x, y in find_valid_pos(x, y, m, n):
                dfs(board, x, y, m, n)

        for i in range(m):
            if board[i][0] == 'O':
                dfs(board, i, 0, m, n)
        for i in range(m):
            if board[i][n-1] == 'O':
                dfs(board, i, n-1, m, n)
        for j in range(n):
            if board[0][j] == 'O':
                dfs(board, 0, j, m, n)
        for j in range(n):
            if board[m-1][j] == 'O':
                dfs(board, m-1, j, m, n)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '|':
                    board[i][j] = 'O'

board = [['O', 'O'], ['O', 'O']]
Solution().solve(board)
print(board)
