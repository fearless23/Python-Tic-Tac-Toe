from game import check_win, create_board, print_board
from game2 import check_player_move

# Initial Data
board_size = 3
no_of_players = 2

# Create initial Board and Print to Console
game = create_board(board_size)

# Switch between players
moves = board_size * board_size
players = [i+1 for i in range(no_of_players)]

# Print Board in starting
print_board(game)

# Run for moves:
for i in range(moves):
    idx = i % no_of_players
    curr_player = players[idx]
    print(f"Hello Player {curr_player}")
    player_made_move = False

    while not player_made_move:
        a, r, c = check_player_move(board_size, game)
        if a:
            player_made_move = True
            game[r-1][c - 1] = curr_player
            print_board(game)

    win, line, p = check_win(game)
    if win:
        print(f"Player {p} wins the game at {line}")
        break
