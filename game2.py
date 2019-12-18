# Player makes a move i.e select a row and column
def check_player_move(board_size, game):
    selRow = int(input("Select Row: "))
    # Check if out of range...
    if(selRow < 1 or selRow > board_size):
        print("Row out of Range")
        return False, None, None

    selCol = int(input("Select Col: "))
    # Check if out of range...
    if(selCol < 1 or selCol > board_size):
        print("Column out of Range")
        return False, selRow, None
    # Check if already marked
    m = game[selRow-1][selCol - 1]
    if m != 0:
        print(f"Position already Marked by Player {m}")
        return False, selRow, selCol
    return True, selRow, selCol
