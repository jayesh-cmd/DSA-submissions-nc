class Solution:
    def solve(self, board: List[List[str]]) -> None:

        row, col = len(board), len(board[0])

        def dfs(r,c):
                if r<0 or r>=row or c<0 or c>=col or board[r][c]!='O':
                    return

                board[r][c] = 'J'
                dfs(r,c+1)
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c-1)

        # When We find the o on the boarder side :-
        for i in range(row):
            for c in range(col):
                if (board[i][c] == 'O') and i == 0 or i == row-1 or c == 0 or c == col-1:
                    dfs(i,c)

        for r in range(row):
            for c in range(col):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        for r in range(row):
            for c in range(col):
                if board[r][c] == 'J':
                    board[r][c] = 'O'