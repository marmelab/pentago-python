import sys

from board import construct_board, add_marble_to_board, is_board_full, get_position_if_valid, rotate_quarter_of_board
from render import print_board

def init_game():
    try:
        board = construct_board()

        while is_board_full(board) == False:
            board = place_marble(board)
            board = rotate_quarter(board)
            
            print_board(board)
        
        print("You finished the game. GJ !")
    except KeyboardInterrupt:
        sys.exit(0)
    finally:
        print("\nIt was fun, see you soon !")



def place_marble(board):
        print_board(board)
        while True:
            input_value = input(" Place a marble: ")

            try:
                return add_marble_to_board(board, input_value)
            except ValueError:
                print(" Please play on a valid & empty cell")
        
def rotate_quarter(board):
    print_board(board, "rotation")
    while True:
        input_value = input(" Now rotate one quarter: ")

        try:
            return rotate_quarter_of_board(board, input_value)
        except ValueError:
            print( "Please enter a valid rotation (1..8): ")

if __name__ == "__main__":
    init_game()
