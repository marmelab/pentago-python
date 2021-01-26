import os
from constant import HALF_BOARD_SIZE


def get_marble_character(value):
    return "◯" if value == 0 else "◉"

"""
board = 2d array
mode = "coords" : display X & Y coordonates on the header and on the left side.
mode = "rotation" : display rotation input to indicate which enter to rotate each quarters
clear_before_printing: If true, clear the console before printing the board.
"""
def print_board(board, mode="coords", clear_before_printing=True):
    if clear_before_printing:
        os.system("clear")

    if mode == "coords":
        print("\n       A  B  C   D  E  F")
        print("     ┌──────────+─────────┐")
    else:
        print("\n      2 ↻             3 ↺")
        print(" 1 ↺ ┌──────────+─────────┐  4 ↻")


    for x, line in enumerate(board, 0):
        if x != 0 and x % HALF_BOARD_SIZE == 0:
            print("     |──────────+─────────|")
        line_values = ""

        for y, value in enumerate(line, 0):
            if y != 0 and y % HALF_BOARD_SIZE == 0:
                line_values = line_values + "|"
            line_values = line_values + " " + get_marble_character(value)

            line_values = line_values + " "
        
        line_values = "  | " + line_values + "|"
        if mode == "coords":
            print("  " + str(x + 1) + line_values)
        else:
            print("   " + line_values)

    if mode == "coords":
        print("     └──────────+─────────┘\n")
    else:
        print(" 8 ↻ └──────────+─────────┘ 5 ↺")
        print("      7 ↺             6 ↻ \n")

