BOARD = [
    [5, 3, ' ', ' ', 7, ' ', ' ', ' ', ' '],
    [6, ' ', ' ', 1, 9, 5, ' ', ' ', ' '],
    [],
    [],
    [],
    [],
    [],
    [],
    []]

def print_board(board):
    width = 9
    height = 9
    border = "+-----------+-----------+-----------+"
    print border
    for row in range(width):
        print "|",
        for col in range(height):
            print BOARD[row][col],
            if (col + 1) % 3 == 0:
                print "|",
            else:
                print " ",
        if (row + 1) % 3 == 0:
            print border
        else:
            print "\n"

print_board(BOARD)
