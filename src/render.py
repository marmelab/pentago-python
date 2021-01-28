import os
from constant.board import HALF_BOARD_SIZE
from constant.ui import *
from win import if_position_is_in_correct_combinations

def get_character(position, value, correct_combinations):
    # Get a character if it's an empty cell, a player cell or a player cell in correct alignment

    if value == 0:
        return UNPLAYED_CHARACTER

    if if_position_is_in_correct_combinations(position, correct_combinations):
        return PLAYER_ALIGNMENT_CHARACTER

    return PLAYER_CHARACTER


def get_player_color(player_value, string):
    # Color a string based on player value

    if player_value == 1:
        return COLOR_YELLOW + string + COLOR_RESET

    if player_value == 2:
        return COLOR_CYAN + string + COLOR_RESET

    return COLOR_RESET + string


"""
    line: A list representing a line in the 2d array.
    For each values, get marble characters
    return line_values ready to be displayed and correctly formatted.
"""


def generate_line_values(x, line, correct_combinations=[]):

    line_values = ""
    for y, value in enumerate(line, 0):
        if y != 0 and y % HALF_BOARD_SIZE == 0:
            line_values = line_values + "|"
        character = get_character((x, y), value, correct_combinations)
        line_values = line_values + " " + get_player_color(value, character)

        line_values = line_values + " "

    return "  |" + line_values + "|"


def print_board_place_marble(board):
    print("\n        A  B  C   D  E  F")
    print(BASE_SPACES + "┌─────────+─────────┐")

    for x, line in enumerate(board, 0):
        if x != 0 and x % HALF_BOARD_SIZE == 0:
            print(BASE_SPACES + "|─────────+─────────|")
        
        print(" " * (BASE_NUMBER_OF_SPACES - 2) + str(x + 1) + " " + generate_line_values(line))

    print(BASE_SPACES + "└─────────+─────────┘\n")

    print("     └─────────+─────────┘\n\n")


def print_board_rotate(board):
    print("\n      2 ↻             3 ↺")
    print("  1 ↺ ┌─────────+─────────┐  4 ↻")

    for x, line in enumerate(board, 0):
        if x != 0 and x % HALF_BOARD_SIZE == 0:
            print(BASE_SPACES + "|─────────+─────────|")

        print(BASE_SPACES + generate_line_values(line))

    print("  8 ↻ └─────────+─────────┘ 5 ↺")
    print("      7 ↺             6 ↻ \n")


def print_board_finished(board, correct_combinations):
    print("\n     The game is finished")
    print("     ┌─────────+─────────┐")

    for x, line in enumerate(board, 0):
        if x != 0 and x % HALF_BOARD_SIZE == 0:
            print("     |─────────+─────────|")

        print("   " + generate_line_values(x, line, correct_combinations))

    print("     └─────────+─────────┘")
    print("\n")


"""
board = 2d array
mode = PRINT_BOARD_PLACE_MARBLE : display X & Y coordonates on the header and on the left side.
mode = PRINT_BOARD_ROTATE : display rotation input to indicate which enter to rotate each quarters
"""


def print_board(board, mode, correct_combinations):

    if mode == PRINT_BOARD_PLACE_MARBLE:
        print_board_place_marble(board)
    elif mode == PRINT_BOARD_ROTATE:
        print_board_rotate(board)
    else:
        print_board_finished(board, correct_combinations)


def print_player(player, current_player_id):
    if player.id == current_player_id:
        print(BASE_SPACES + "| " + get_marble_character(player.id) + " " + player.name + " |", end="")
    else:
        print(BASE_SPACES + get_marble_character(player.id) + " " + player.name, end="")


def print_players(players, current_player_id):
    # Constant used to display box around player 1's nickname or player 2.
    BOX_SPACES = BASE_SPACES + " " * (players[0].name_length + 2 * MINIMAL_SPACES_PLAYER) * (current_player_id - 1)

    # Constant to calculate length of current player name
    # + 4 = 1 for the marble, 1 for marble left space and 2 around player name
    BORDER_LENGTH = "─" * (players[current_player_id - 1].name_length + MINIMAL_SPACES_PLAYER)
    
    # If current player is 1, draw around his nickname a box.
    # Instead draw this box on the second player.
    print(BOX_SPACES + "┌" + BORDER_LENGTH + "┐")
    print_player(players[0], current_player_id)
    print_player(players[1], current_player_id)
    print("\n" + BOX_SPACES + "└" + BORDER_LENGTH + "┘")

def print_game_result(players, correct_combinations):
    correct_combinations_length = len(correct_combinations)
    if correct_combinations_length == 0:
        print("Nobody of you be able to align 5 marbles. \n It's a draw !")
    elif correct_combinations_length == 1:
        player = players[correct_combinations[0]['player_id'] - 1]

        winner_string = "GJ " + player.name + ", You win !"
        print(get_player_color(player.id, winner_string))
    else:
        print('Not implemented yet !')

"""
game = structure containing board & players
mode = PRINT_BOARD_PLACE_MARBLE : display X & Y coordonates on the header and on the left side.
mode = PRINT_BOARD_ROTATE : display rotation input to indicate which enter to rotate each quarters
clear_before_printing: If true, clear the console before printing the board.
"""


def print_game(game, print_board_mode=PRINT_BOARD_PLACE_MARBLE, clear_before_printing=True, correct_combinations=[]):
    if clear_before_printing:
        os.system("clear")
    print_board(game.board, print_board_mode, correct_combinations)

    if print_board_mode == PRINT_BOARD_FINISHED:
        print_game_result(game.players, correct_combinations)
    else:
        print_players(game.players, game.current_player_id)
