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
            
            result = add_marble_to_board(board, input_value)
            
            if result != None:
                board = result
                break
            else:
                print("Please play on a valid & empty cell")
        return board

if __name__ == "__main__":
    init_game()
