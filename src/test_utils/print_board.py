import sys
from render import print_board

def print_board_if_verbosity_is_set(board):
    if "-v" in sys.argv:
        print_board(board, False)
