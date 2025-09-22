class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(r, c, k):
            for i in range(9):
                if board[i][c] == k:  # Check column
                    return False
                if board[r][i] == k:  # Check row
                    return False
                if board[3*(r//3) + i//3][3*(c//3) + i%3] == k:  # Check 3x3 box
                    return False
            return True

        def solve():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        for k in map(str, range(1, 10)):
                            if is_valid(r, c, k):
                                board[r][c] = k
                                if solve():
                                    return True
                                board[r][c] = "."
                        return False
            return True

        solve()
