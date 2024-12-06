import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def computer_move(board):
    # Find all empty cells
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_cells) if empty_cells else None

def main():
    print("Welcome to Tic-Tac-Toe!")
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    computer = "O"

    print_board(board)

    while True:
        # Player's turn
        row, col = -1, -1
        while not (0 <= row < 3 and 0 <= col < 3 and board[row][col] == " "):
            try:
                row, col = map(int, input("Enter your move (row and column 0-2, separated by space): ").split())
            except ValueError:
                print("Invalid input. Please enter two numbers between 0 and 2 separated by a space.")

        board[row][col] = player
        print_board(board)

        if check_winner(board, player):
            print("Congratulations! You win!")
            break

        if is_full(board):
            print("It's a tie!")
            break

        # Computer's turn
        print("Computer's turn...")
        move = computer_move(board)
        if move:
            board[move[0]][move[1]] = computer
            print_board(board)

            if check_winner(board, computer):
                print("Computer wins! Better luck next time.")
                break

        if is_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
