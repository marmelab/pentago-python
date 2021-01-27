import sys
from constant.ui import PRINT_BOARD_PLACE_MARBLE, PRINT_BOARD_ROTATE
from game import construct_game, player_finished_his_turn

from board import add_marble_to_board, is_board_full, get_position_if_valid, rotate_quarter_of_board

from render import print_game


def init_game():
    try:
        game = construct_game()

        while is_board_full(game["board"]) == False:
            print_game(game, PRINT_BOARD_PLACE_MARBLE)
            game["board"] = ask_player_to_place_marble(
                game["board"], game["current_player_id"]
            )

            print_game(game, PRINT_BOARD_ROTATE)
            game["board"] = ask_player_to_rotate_quarter(game["board"])

            game["current_player_id"] = player_finished_his_turn(
                game["current_player_id"]
            )

        print("You finished the game. GJ !")
    except KeyboardInterrupt:
        sys.exit(0)
    finally:
        print("\nIt was fun, see you soon !")


def ask_player_to_place_marble(board, current_player_id):
    input_value_is_wrong = True;

    while input_value_is_wrong:
        input_value = input(" Place a marble: ")

        try:
            board = add_marble_to_board(board, current_player_id, input_value)
            input_value_is_wrong = False
        except ValueError:
            print(" Please play on a valid & empty cell")
            input_value_is_wrong = True;

    return board

def ask_player_to_rotate_quarter(board):
    input_value_is_wrong = True;
    
    while input_value_is_wrong:
        input_value = input(" Now rotate one quarter: ")

        try:
            board = rotate_quarter_of_board(board, input_value)
            input_value_is_wrong = False
        except ValueError:
            print("Please enter a valid rotation (1..8): ")
            input_value_is_wrong = True

    return board

if __name__ == "__main__":
    init_game()
