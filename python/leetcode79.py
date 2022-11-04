from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ncols, nrows = len(board), len(board[0])
        visited = [[False for _ in range(nrows)] for _ in range(ncols)]
        for i in range(ncols):
            for j in range(nrows):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if self.dfs(board, i, j, 1, word, visited):
                        return True
                    visited[i][j] = False
        return False


    def dfs(self, board, i, j, n, word, visited):
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if n == len(word):
            return True

        next_pos = []
        for delta in deltas:
            next_i = i + delta[0]
            next_j = j + delta[1]
            if 0 <= next_i < len(board) and 0 <= next_j < len(board[0]) \
                and not visited[next_i][next_j] and board[next_i][next_j] == word[n]:
                next_pos.append((next_i, next_j))

        for pos in next_pos:
            visited[pos[0]][pos[1]] = True
            if self.dfs(board, pos[0], pos[1], n+1, word, visited):
                return True
            visited[pos[0]][pos[1]] = False
        return False

