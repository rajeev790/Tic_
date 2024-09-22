def print_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_winner(board, player):
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), # Horizontal
                        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Vertical
                        (0, 4, 8), (2, 4, 6)]            # Diagonal
    
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def is_draw(board):
    return all(position != ' ' for position in board)

def tic_tac_toe():
    while True:
        board = [' ' for _ in range(9)]
        current_player = 'X'
        game_over = False

        while not game_over:
            print_board(board)
            try:
                move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
                if board[move] == ' ':
                    board[move] = current_player
                else:
                    print("Invalid move! The cell is already taken. Try again.")
                    continue
            except (ValueError, IndexError):
                print("Invalid input! Please enter a number between 1 and 9.")
                continue

            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                game_over = True
            elif is_draw(board):
                print_board(board)
                print("It's a draw!")
                game_over = True
            else:
                current_player = 'O' if current_player == 'X' else 'X'

        restart = input("Do you want to play again? (y/n): ").lower()
        if restart != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    tic_tac_toe()
