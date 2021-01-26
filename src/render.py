import os
from constant import BOARD_SIZE

def get_marble_character(value):
    return "◯" if value == 0 else "◉"
    
def print_board(board, clear_before_printing = True):
    
    if clear_before_printing:
        os.system("clear")

    # Used to detect when adding a line for drawing quarters.
    HALF_BOARD_SIZE = (BOARD_SIZE / 2)

    print("\n      A  B  C   D  E  F")
    print("   ┌──────────+─────────┐")
    for x, line in enumerate(board, 0):
        if x != 0 and x % HALF_BOARD_SIZE == 0:
            print("   |──────────+─────────|")
        line_values = ""

        for y, value in enumerate(line, 0):
            if y != 0 and y % HALF_BOARD_SIZE == 0:
                line_values = line_values + "|"
            line_values = line_values + " " + get_marble_character(value)
            
            line_values = line_values + " "

        print(" " + str(x + 1) + " | " + line_values + "|")
    print("   └──────────+─────────┘\n")
