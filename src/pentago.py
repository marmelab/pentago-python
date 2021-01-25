from board import construct_board, print_board, add_marble_to_board, is_board_full, get_position_if_valid

def init_game():
    board = construct_board()

    while is_board_full(board) == False:
        board = play_turn(board)
    
    print_board(board)
    print("You finished the game. GJ !")



def play_turn(board):
        print_board(board)
        while True:
            input_value = input("Place a marble:")
            
            position = get_position_if_valid(board, input_value)
            
            if position != None:
                add_marble_to_board(board, position)
                break
            else:
                print("Please play on a valid & empty cell")
        return board

if __name__ == "__main__":
    init_game()
