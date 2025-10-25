def find_winner_tic_tac_toe(moves):
    """
    Problem: Find Winner on a Tic Tac Toe Game
    
    Given an array of moves, determine the winner:
    - "A" wins if player A has 3 in a row/column/diagonal
    - "B" wins if player B has 3 in a row/column/diagonal  
    - "Draw" if board is full with no winner
    - "Pending" if game is still ongoing
    
    Approach: Simulate the game and check for winners after each move
    Time Complexity: O(n) where n is number of moves
    Space Complexity: O(1) - fixed 3x3 board
    
    Example: moves = [[0,0],[2,0],[1,1],[1,0],[2,1],[0,1],[0,2],[0,1],[2,2]]
             Result: "A" (A wins with diagonal)
    """
    # Initialize 3x3 board
    board = [['' for _ in range(3)] for _ in range(3)]
    
    def check_winner(board):
        """Check if there's a winner on the current board."""
        # Check rows
        for row in board:
            if row[0] == row[1] == row[2] != '':
                return row[0]
        
        # Check columns
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != '':
                return board[0][col]
        
        # Check main diagonal (top-left to bottom-right)
        if board[0][0] == board[1][1] == board[2][2] != '':
            return board[0][0]
        
        # Check anti-diagonal (top-right to bottom-left)
        if board[0][2] == board[1][1] == board[2][0] != '':
            return board[0][2]
        
        return None
    
    def is_board_full(board):
        """Check if the board is completely filled."""
        for row in board:
            for cell in row:
                if cell == '':
                    return False
        return True
    
    # Simulate the game
    for i, (row, col) in enumerate(moves):
        # Player A moves on even indices (0, 2, 4, ...)
        # Player B moves on odd indices (1, 3, 5, ...)
        current_player = 'A' if i % 2 == 0 else 'B'
        
        # Place the move
        board[row][col] = current_player
        
        print(f"Move {i+1}: Player {current_player} plays [{row}, {col}]")
        print_board(board)
        
        # Check for winner after the move
        winner = check_winner(board)
        if winner:
            return winner
        
        # Check for draw (board full and no winner)
        if is_board_full(board):
            return "Draw"
    
    # Game is still pending
    return "Pending"

def print_board(board):
    """Helper function to visualize the board."""
    print("Current board:")
    for row in board:
        print(" | ".join([cell if cell else ' ' for cell in row]))
        print("-" * 9)
    print()

def test_tic_tac_toe():
    """Test the tic tac toe solution with different scenarios."""
    
    print("=== TIC TAC TOE GAME WINNER ===\n")
    
    # Test case 1: A wins with diagonal
    print("Test 1: A wins with diagonal")
    moves1 = [[0,0],[2,0],[1,1],[1,0],[2,1],[0,1],[0,2],[0,1],[2,2]]
    result1 = find_winner_tic_tac_toe(moves1)
    print(f"Result: {result1}\n")
    
    # Test case 2: B wins with row
    print("Test 2: B wins with row")
    moves2 = [[0,0],[1,0],[0,1],[1,1],[0,2],[1,2]]
    result2 = find_winner_tic_tac_toe(moves2)
    print(f"Result: {result2}\n")
    
    # Test case 3: Draw
    print("Test 3: Draw scenario")
    moves3 = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
    result3 = find_winner_tic_tac_toe(moves3)
    print(f"Result: {result3}\n")
    
    # Test case 4: Pending (game not finished)
    print("Test 4: Pending game")
    moves4 = [[0,0],[1,1],[0,1]]
    result4 = find_winner_tic_tac_toe(moves4)
    print(f"Result: {result4}\n")

# Original test case from the code
print("=== ORIGINAL TEST CASE ===")
moves = [[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]
result = find_winner_tic_tac_toe(moves)
print(f"Winner: {result}")

print("\n" + "="*50)
# Run comprehensive tests
test_tic_tac_toe()
