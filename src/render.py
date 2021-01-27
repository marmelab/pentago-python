import os
from constant import HALF_BOARD_SIZE, PRINT_BOARD_PLACE_MARBLE, PRINT_BOARD_ROTATE, COLOR_RESET, COLOR_YELLOW, COLOR_CYAN

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
clear_before_printing: If true, clear the console before printing the board.
"""
def print_board(board, mode=PRINT_BOARD_PLACE_MARBLE, clear_before_printing=True):
    if clear_before_printing:
        os.system("clear")

    if mode == PRINT_BOARD_PLACE_MARBLE:
        print_board_place_marble(board)
    else:
        print_board_rotate(board)

def print_players(players, current_player_id):

    # If current player is 1, draw around his nickname a box.
    # Instead draw this box on the second player.
    if current_player_id == players[0]["id"]:
        print("    ┌────────────┐")
        print("    | " + get_marble_character(players[0]["id"]) + " " + players[0]["name"] + " | ", end="")
        print("   " + get_marble_character(players[1]["id"]) + " " + players[1]["name"])
        print("    └────────────┘")
    else:
        print("                ┌────────────┐")
        print("   " + get_marble_character(players[0]["id"]) + " " + players[0]["name"], end="")
        print("   | " + get_marble_character(players[1]["id"]) + " " + players[1]["name"] + " | ")
        print("                └────────────┘")



def print_game(game, print_board_mode, clear_before_printing=True):
    if clear_before_printing:
        os.system("clear")

    print_board(game["board"], print_board_mode)

    print_players(game["players"], game["current_player_id"])
