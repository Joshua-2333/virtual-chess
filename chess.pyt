import sys
import copy

# Starting positions of all chess pieces
STARTING_PIECES = {
    'a8': 'bR', 'b8': 'bN', 'c8': 'bB', 'd8': 'bQ',
    'e8': 'bK', 'f8': 'bB', 'g8': 'bN', 'h8': 'bR',
    'a7': 'bP', 'b7': 'bP', 'c7': 'bP', 'd7': 'bP',
    'e7': 'bP', 'f7': 'bP', 'g7': 'bP', 'h7': 'bP',

    'a2': 'wP', 'b2': 'wP', 'c2': 'wP', 'd2': 'wP',
    'e2': 'wP', 'f2': 'wP', 'g2': 'wP', 'h2': 'wP',
    'a1': 'wR', 'b1': 'wN', 'c1': 'wB', 'd1': 'wQ',
    'e1': 'wK', 'f1': 'wB', 'g1': 'wN', 'h1': 'wR'
}

WHITE_SQUARE = "||"
BLACK_SQUARE = "  "

BOARD_TEMPLATE = """
    a    b    c    d    e    f    g    h
   ____ ____ ____ ____ ____ ____ ____ ____
  ||||||    ||||||    ||||||    ||||||    |
8 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
7 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
6 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
5 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
4 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
3 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
2 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
1 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
"""

def print_chessboard(board):
    squares = []
    is_white_square = True

    for y in "87654321":
        for x in "abcdefgh":
            square = x + y

            if square in board:
                squares.append(board[square])
            else:
                if is_white_square:
                    squares.append(WHITE_SQUARE)
                else:
                    squares.append(BLACK_SQUARE)

            # Switch colors
            is_white_square = not is_white_square

        # Switch again at end of row
        is_white_square = not is_white_square

    print(BOARD_TEMPLATE.format(*squares))


# Main game board
main_board = copy.copy(STARTING_PIECES)

print("Interactive Chessboard Simulator")
print("Commands:")
print(" move <from> <to>")
print(" remove <square>")
print(" set <square> <piece>")
print(" reset")
print(" clear")
print(" fill <piece>")
print(" quit")

while True:
    print_chessboard(main_board)

    response = input("> ").split()

    if len(response) == 0:
        continue

    command = response[0]

    if command == "move":
        if len(response) == 3:
            old_square = response[1]
            new_square = response[2]

            if old_square in main_board:
                main_board[new_square] = main_board[old_square]
                del main_board[old_square]

    elif command == "remove":
        if len(response) == 2:
            square = response[1]
            if square in main_board:
                del main_board[square]

    elif command == "set":
        if len(response) == 3:
            square = response[1]
            piece = response[2]
            main_board[square] = piece

    elif command == "reset":
        main_board = copy.copy(STARTING_PIECES)

    elif command == "clear":
        main_board = {}

    elif command == "fill":
        if len(response) == 2:
            piece = response[1]
            for y in "87654321":
                for x in "abcdefgh":
                    main_board[x + y] = piece

    elif command == "quit":
        sys.exit()

    else:
        print("Unknown command.")