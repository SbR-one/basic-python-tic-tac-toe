import numpy as np

def create_board():
  """Creates a 3x3 tic-tac-toe board.

    Returns:
      A 3x3 Numpy array representing the board.
  """
  return np.array([["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]])

def print_board(board):
  """Prints the tic-tac-toe board.
  Args:
    board: The 3x3 Numpy array representing the board.
  """
  for row in board:
    print(" | ".join(row))
    print("----------")

def check_win(board, player):
  """Checks if the given player has won the game.

  Args:
    board: The 3x3 Numpy array representing the board.
    player: The player to check for a win 'X' or 'O').

  Returns:
  True if the player has won, False otherwise.
  """
  # Check rows
  for row in board:
    if all(cell == player for cell in row):
      return True

    # Check columns
    for col in range(3):
      if all(board[row][col] == player for row in range(3)):
        return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
      return True
    if all(board[i][2 - i] == player for i in range(3)):
      return True

  return False

def check_tie(board):
  """Checks if the game is a tie.

  Args:
    board: The 3x3 Numpy array representing the board.

  Returns:
    True if the game is a tie, False otherwise. The game is a tie if
    all cells on the board are filled without a winner.
  """
  return all(cell != "-" for cell in board.flatten())

def play_game():
  """Plays the tic-tac-toe game."""
  board = create_board()
  current_player = "X"

  while True:
    print_board(board)
    print(f"Player {current_player}'s turn.")

    while True:
      try:
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
        if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == "-":
          break
        else:
          print("Invalid move. Try again")
      except ValueError:
          print("Invalid input. Please enter numbers.")
    board[row][col] = current_player

    if check_win(board, current_player):
      print_board(board)
      print(f"Player {current_player} wins!")
      break
    elif check_tie(board):
      print_board(board)
      print("It's a tie!")
      break
    else:
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
  play_game()

