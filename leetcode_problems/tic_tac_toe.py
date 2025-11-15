class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        A = []
        B = []
        wins = [
            # Rows
            [[0, 0], [0, 1], [0, 2]],
            [[1, 0], [1, 1], [1, 2]],
            [[2, 0], [2, 1], [2, 2]],
            # Columns
            [[0, 0], [1, 0], [2, 0]],
            [[0, 1], [1, 1], [2, 1]],
            [[0, 2], [1, 2], [2, 2]],
            # Diagonals
            [[0, 0], [1, 1], [2, 2]],
            [[0, 2], [1, 1], [2, 0]],
        ]
        for i in range(0, len(moves)):
            if i % 2 == 0:
                A.append(moves[i])
            else:
                B.append(moves[i])
        for win in wins:
            if all(pos in A for pos in win):
                return "A"
            if all(pos in B for pos in win):
                return "B"
        # If all 9 moves are used and no winner → Draw
        if len(moves) == 9:
            return "Draw"
        # Otherwise game not finished yet
        return "Pending"


print(Solution().tictactoe([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]))
