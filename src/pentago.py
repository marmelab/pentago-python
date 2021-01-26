from board import construct_board, add_marble_to_board, is_board_full, get_position_if_valid
from render import print_board

def init_game():

    board = construct_board()

    while is_board_full(board) == False:
        board = play_turn(board)
    
    print_board(board)
    print("You finished the game. GJ !")



def play_turn(board):
        print_board(board)
        while True:
            input_value = input("Place a marble: ")
            try:
                return add_marble_to_board(board, input_value)
            except ValueError:
                print("Please play on a valid & empty cell")
        

if __name__ == "__main__":
    init_game()
