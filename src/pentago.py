import sys

from board import construct_board, add_marble_to_board, is_board_full, get_position_if_valid, rotate_quarter_of_board
from render import print_board
from constant import PRINT_BOARD_PLACE_MARBLE, PRINT_BOARD_ROTATE

def init_game():
    try:
        board = construct_board()

        while is_board_full(board) == False:
            board = ask_player_to_place_marble(board)
            board = ask_player_to_rotate_quarter(board)

        print("You finished the game. GJ !")
    except KeyboardInterrupt:
        sys.exit(0)
    finally:
        print("\nIt was fun, see you soon !")



def ask_player_to_place_marble(board):
        print_board(board, PRINT_BOARD_PLACE_MARBLE)
        while True:
            input_value = input(" Place a marble: ")

            try:
                return add_marble_to_board(board, input_value)
            except ValueError:
                print(" Please play on a valid & empty cell")
        
def ask_player_to_rotate_quarter(board):
    print_board(board, PRINT_BOARD_ROTATE)
    while True:
        input_value = input(" Now rotate one quarter: ")

        try:
            return rotate_quarter_of_board(board, input_value)
        except ValueError:
            print( "Please enter a valid rotation (1..8): ")

if __name__ == "__main__":
    init_game()
