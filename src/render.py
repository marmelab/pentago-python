import os
from constant.board import HALF_BOARD_SIZE
from constant.ui import PRINT_BOARD_PLACE_MARBLE, PRINT_BOARD_ROTATE, COLOR_RESET, COLOR_YELLOW, COLOR_CYAN

# Color a marble char based on player value
def get_marble_character(value):

    if value == 1:
        return COLOR_YELLOW + "◉" + COLOR_RESET
    
    if value == 2:
        return COLOR_CYAN + "◉" + COLOR_RESET

    return "◯"

"""
    line: A list representing a line in the 2d array.
    For each values, get marble characters
    return line_values ready to be displayed and correctly formatted.
"""
def generate_line_values(line):
    line_values = ""
    for y, value in enumerate(line, 0):
        if y != 0 and y % HALF_BOARD_SIZE == 0:
            line_values = line_values + "|"
        line_values = line_values + " " + get_marble_character(value)

        line_values = line_values + " "
    
    return "  | " + line_values + "|"

def print_board_place_marble(board):
    print("\n        A  B  C   D  E  F")
    print("     ┌──────────+─────────┐")

    for x, line in enumerate(board, 0):
        if x != 0 and x % HALF_BOARD_SIZE == 0:
            print("     |──────────+─────────|")
        
        print("  " + str(x + 1) + generate_line_values(line))

    print("     └──────────+─────────┘\n")

def print_board_rotate(board):
    print("\n      2 ↻             3 ↺")
    print(" 1 ↺ ┌──────────+─────────┐  4 ↻")

    for x, line in enumerate(board, 0):
        if x != 0 and x % HALF_BOARD_SIZE == 0:
            print("     |──────────+─────────|")

        print("   " + generate_line_values(line))

    print(" 8 ↻ └──────────+─────────┘ 5 ↺")
    print("      7 ↺             6 ↻ \n")

"""
board = 2d array
mode = PRINT_BOARD_PLACE_MARBLE : display X & Y coordonates on the header and on the left side.
mode = PRINT_BOARD_ROTATE : display rotation input to indicate which enter to rotate each quarters
"""
def print_board(board, mode=PRINT_BOARD_PLACE_MARBLE):

    if mode == PRINT_BOARD_PLACE_MARBLE:
        print_board_place_marble(board)
    else:
        print_board_rotate(board)

def print_player(player, current_player_id):
    if player.id == current_player_id:
        print("    | " + get_marble_character(player.id) + " " + player.name + " |", end="")
    else:
        print("    " + get_marble_character(player.id) + " " + player.name, end="")


def print_players(players, current_player_id):

    # Constant used to display box around player 1's nickname or player 2.

    BOX_SPACES = " " * 14 * (current_player_id - 1)

    # If current player is 1, draw around his nickname a box.
    # Instead draw this box on the second player.

    print(BOX_SPACES + "    ┌────────────┐")
    print_player(players[0], current_player_id)
    print_player(players[1], current_player_id)
    print("\n" + BOX_SPACES + "    └────────────┘")


"""
game = structure containing board & players
mode = PRINT_BOARD_PLACE_MARBLE : display X & Y coordonates on the header and on the left side.
mode = PRINT_BOARD_ROTATE : display rotation input to indicate which enter to rotate each quarters
clear_before_printing: If true, clear the console before printing the board.
"""
def print_game(game, print_board_mode, clear_before_printing=True):
    if clear_before_printing:
        os.system("clear")

    print_board(game.board, print_board_mode)

    print_players(game.players, game.current_player_id)
