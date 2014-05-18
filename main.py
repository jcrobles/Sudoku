BOARD = [
    [6, ' ', 2, ' ', 8, ' ', 1, ' ', 9],
    [3, ' ', 9, 1, 5, ' ', ' ', ' ', 2],
    [8, ' ', ' ', 9, ' ', 6, ' ', 3, 4],
    [' ', 3, 4, ' ', 1, ' ', 9, 2, ' '],
    [' ', 6, ' ', 3, ' ', 9, 5, 7, ' '],
    [' ', 9, 1, 6, ' ', 2, ' ', 4, ' '],
    [4, ' ', ' ', ' ', 9, 1, 2, ' ', 5],
    [' ', 5, 7, ' ', ' ', ' ', 4, 9, 3],
    [9, 2, ' ', 5, 3, 4, ' ', ' ', ' ']]

def print_board(board):
    width = 9
    height = 9
    border = "+-----------+-----------+-----------+"
    print border
    for row in range(width):
        print "|",
        for col in range(height):
            print board[row][col],
            if col == 8:
                print "|"
            elif (col + 1) % 3 == 0:
                print "|",
            else:
                print " ",
        if (row + 1) % 3 == 0:
            print border

def test_tile(row, col, board):
    possibles = []
    if isinstance(board[row][col], int):
        return [board[row][col]]

    for i in range(9):
        if test_row(row, col, i+1, board) and \
           test_col(row, col, i+1, board) and \
           test_square(row, col, i+1, board):
            possibles.append(i+1)
    return possibles

def test_row(row, col, test, board):
    if isinstance(board[row][col], int):
       return False
    for x in range(9):
        if board[row][x] == test:
            return False
    return True

def test_col(row, col, test, board):
    if isinstance(board[row][col], int):
        return False
    for x in range(9):
        if board[x][col] == test:
            return False
    return True

def test_square(row, col, test, board):
    square_row = int(row/3)*3
    square_col = int(col/3)*3

    for row_local in range(3):
        for col_local in range(3):
            if board[square_row+row_local][square_col+col_local] == test:
                return False
    return True

def solved(board):
    for row in range(9):
        for col in range(9):
            if not isinstance(board[row][col], int):
                return False
    return True

def solve_board(board):
    while True:
        if solved(board):
            return
        # do magic!

print_board(BOARD)
solve_board(BOARD)
print_board(BOARD)
