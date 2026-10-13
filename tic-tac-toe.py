def print_board(board):
    print()
    for i in range(0, 9, 3):
        row = []
        for j in range(i, i + 3):
            row.append(board[j])
        print(" " + " | ".join(row))
        if i < 6:
            print("---+---+---")
    print()


def check_winner(board, player):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


def play_game():
    board = [str(i) for i in range(1, 10)]
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print("Choose a number from 1 to 9 to make your move.")

    while True:
        print_board(board)
        choice = input(f"Player {current_player}, choose a cell: ")

        if not choice.isdigit() or choice not in board:
            print("Invalid move! Try again.")
            continue

        position = int(choice) - 1
        board[position] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if all(cell in ["X", "O"] for cell in board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


if --name-- == "--main--":
    play_game()