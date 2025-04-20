def play_tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!\n")
    
    # Step 1: Ask player 1 to choose their symbol
    player1_symbol = input("Player 1, choose 'X' or 'O': ").upper()
    while player1_symbol not in ['X', 'O']:
        print("Invalid choice. Please choose 'X' or 'O'.")
        player1_symbol = input("Player 1, choose 'X' or 'O': ").upper()
    
    player2_symbol = 'O' if player1_symbol == 'X' else 'X'





    
    # Initialize the board with numbers 1-9
    board = [str(i) for i in range(1, 10)]
    
    current_player = 1
    current_symbol = player1_symbol
    game_active = True
    
    def display_board():
        print("\nCurrent Board:")
        for i in range(0, 9, 3):
            print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
            if i < 6:
                print("---")
    
    def check_winner():





        # All possible winning combinations (rows, columns, diagonals)
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        
        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]]:
                return board[combo[0]]
        return None
    



    
    # Main game loop
    while game_active:
        display_board()
        
        # Step 2: Ask for player's move
        move = input(f"\nPlayer {current_player}'s turn. Enter your move (1-9): ")
        
        
        # Validate input
        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
            
        move_index = int(move) - 1  # Convert to 0-8 index


        
        # Step 3: Check if position is already taken
        if board[move_index] in ['X', 'O']:
            print("That position is already taken. Please choose another.")
            continue
        
            
        # Update board with current player's symbol
        board[move_index] = current_symbol

        
        # Step 5: Check for winner
        winner = check_winner()
        if winner:
            display_board()
            print(f"\nPlayer {current_player} is the winner! Thanks for playing Tic-Tac-Toe!")
            game_active = False
            break
        
            
        # Step 6: Check for tie (full board)
        if all(cell in ['X', 'O'] for cell in board):
            display_board()
            print("\nIt's a draw! Thanks for playing Tic-Tac-Toe!")
            game_active = False
            break
        
            
        # Switch players for next turn
        current_player = 2 if current_player == 1 else 1
        current_symbol = player2_symbol if current_symbol == player1_symbol else player1_symbol

if __name__ == "__main__":
    play_tic_tac_toe()
