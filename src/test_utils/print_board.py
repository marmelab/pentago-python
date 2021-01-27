import sys
from render import print_board
from constant import PRINT_BOARD_PLACE_MARBLE

def print_board_if_verbosity_is_set(board):
    if "-v" in sys.argv:
        print_board(board, PRINT_BOARD_PLACE_MARBLE, False)
