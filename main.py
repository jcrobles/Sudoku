BOARD = [
    [5, 3, ' ', ' ', 7, ' ', ' ', ' ', ' '],
    [6, ' ', ' ', 1, 9, 5, ' ', ' ', ' '],
    [' ', 9, 8, ' ', ' ', ' ', ' ', 6, ' '],
    [8, ' ', ' ', ' ', 6, ' ', ' ', ' ', 3,],
    [4, ' ', ' ', 8, ' ', 3, ' ', ' ', 6],
    [7, ' ', ' ', ' ', 2, ' ', ' ', ' ', 6],
    [' ', 6, ' ', ' ', ' ', ' ', 2, 8, ' '],
    [' ', ' ', ' ', 4, 1, 9, ' ', ' ', 5],
    [' ', ' ', ' ', ' ', 8, ' ', ' ', 7, 9]]

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

print_board(BOARD)
