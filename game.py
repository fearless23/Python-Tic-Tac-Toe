import os


# all_same
def all_same(l):
    if l[0] == 0:
        return False
    for i in range(1, len(l)):
        if l[i] != l[0]:
            return False
    return True


# create initial Board
def create_board(board_size):
    game = []
    for i in range(board_size):
        col = [0 for j in range(board_size)]
        game.append(col)
    return game


# Check Any one wins
def check_win(board):
    board_size = len(board)
    for i in range(board_size):
        # Get horizontal lines and check
        if all_same(board[i]):
            return True, "Row "+str(i+1), board[i][0]

        # Get vertical lines and check (faster)
        col = [board[j][i] for j in range(board_size)]
        if all_same(col):
            return True, "Col "+str(i+1), col[0]

    # Get diagonal (\) line and check (faster)
    d1 = [board[i][i] for i in range(board_size)]
    if all_same(d1):
        return True, "Diagonal (\\)", d1[0]

    # Get diagonal (/) line and check (faster)
    d2 = [board[i][board_size - i - 1] for i in range(board_size)]
    if all_same(d2):
        return True, "Diagonal (/)", d2[0]

    return False, None, None


# Internal FN
def ss(n):
    s = [str(i+1) for i in range(n)]
    return "  ".join(s)


# Print Board
def print_board(board):
    os.system('clear')
    print(f"  COL -  {ss(len(board))}")
    for i in range(len(board)):
        print(f"  R{i+1} -- {board[i]}")
    print("  ")
