class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        def nQueens(rows):
            if rows == n:
                ans.append(["".join(row) for row in board])
                return
            for j in range(n):
                if self.isSafe(board,rows,j,n):
                    board[rows][j] = 'Q'
                    nQueens(rows+1)
                    board[rows][j] = '.'
        nQueens(0)
        return ans
    def isSafe(self,board,rows,col,n):
        for i in range(n):
            if board[rows][i] == 'Q':
                return False
        for i in range(n):
            if board[i][col] == 'Q':
                return False
        r,c = rows,col
        while r >=0 and c >= 0:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c -= 1
        r,c = rows,col
        while r >=0 and c < n :
            if board[r][c] == 'Q':
                return False
            r -= 1
            c += 1
        return True
        
            
            
