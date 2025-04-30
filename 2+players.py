def print_board(board):
    for row in board:
        print(" | ".join(cell if cell else " " for cell in row))
        print("-" * (len(board) * 4 - 1))

def check_winner(board, symbol):
    n = len(board)

    # Check rows
    for row in board:
        if all(cell == symbol for cell in row):
            return True

    # Check columns
    for col in range(n):
        if all(board[row][col] == symbol for row in range(n)):
            return True

    # Check main diagonal
    if all(board[i][i] == symbol for i in range(n)):
        return True

    # Check anti-diagonal
    if all(board[i][n - 1 - i] == symbol for i in range(n)):
        return True

    return False

def is_full(board):
    return all(all(cell for cell in row) for row in board)

def play_game():
    # Get board size
    while True:
        try:
            board_size = int(input("Enter board size (minimum 3): "))
            if board_size >= 3:
                break
            else:
                print("Board size must be at least 3.")
        except ValueError:
            print("Please enter a valid number.")
            

    board = [[None for _ in range(board_size)] for _ in range(board_size)]

    # Get player info
    num_players = int(input("Enter number of players (2 or more): "))
    players = []
    symbols = set()

    for i in range(num_players):
        name = input(f"Enter name for Player {i + 1}: ")
        symbol = input(f"Enter symbol for {name} (one character, e.g., X, O, @, #): ")
        while symbol in symbols or len(symbol) != 1:
            symbol = input("Symbol already taken or invalid. Choose a different one: ")
        players.append({"name": name, "symbol": symbol})
        symbols.add(symbol)

    current_player_idx = 0

    while True:
        print_board(board)
        player = players[current_player_idx]
        print(f"{player['name']}'s turn ({player['symbol']})")

        try:
            row = int(input(f"Enter row (0 to {board_size - 1}): "))
            col = int(input(f"Enter column (0 to {board_size - 1}): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if not (0 <= row < board_size and 0 <= col < board_size):
            print(f"Row and column must be between 0 and {board_size - 1}.")
            continue

        if board[row][col] is not None:
            print("That spot is already taken.")
            continue

        board[row][col] = player['symbol']

        if check_winner(board, player['symbol']):
            print_board(board)
            print(f"🎉 {player['name']} wins! 🎉")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player_idx = (current_player_idx + 1) % num_players

play_game()
