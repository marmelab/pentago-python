from copy import deepcopy
from constant import ARRAY_SIZE

def construct_board():
    return [[0] * ARRAY_SIZE for _ in range(ARRAY_SIZE)]


def is_board_full(board):
    for x, line in enumerate(board, 0):
        for y, value in enumerate(line, 0):
            if value == 0:
                return False
    return True


"""
get_position_if_valid(board: 2 dim array, user_value: string (e.g "A1"))
Check if position asked for user is correct for validate multiple conditions :

- user_value is a string which contain only 2 chars
- user_value[0] & user_value[1] refer to an existing cell in board (in boundaries)
- This cell is empty.

If correct, return a tuple that containing array friendly coords (1,2).
If wrong, return None.

"""
def get_position_if_valid(board, user_value):
    try:
        if len(user_value) != 2:
            return None

        x = int(user_value[1]) - 1

        """
        See https://stackoverflow.com/questions/5927149/get-character-position-in-alphabet
        Each chars have a unicode point (an integer).
        ord("a") = 97, ord("b") = 98, ord("z") = 122.
        To convert for an array case, simply remove unicode point from "a" to this chars.
        Don't forget to lowercase this chars because uppercase has different unicode point.
        """
        y = ord(user_value[0].lower()) - 97

        r = range(0, ARRAY_SIZE)

        # If position is outside boundaries or on an already filled position.
        if x not in r or y not in r or board[x][y] != 0:
            return None

        # Return 2 dim array relative position (e.g (0, 0))
        return (x, y)
    except:
        return None


def add_marble_to_board(board, user_value):
    position = get_position_if_valid(board, user_value)
    if position == None:
        return None

    board = deepcopy(board)
    board[position[0]][position[1]] = 1
    return board


def get_marble_character(value):
    return "◯" if value == 0 else "◉"


def print_board(board):
    print("\n      A  B  C  D  E  F")
    print("   ┌───────────────────┐")
    for x, line in enumerate(board, 0):
        line_values = ""
        for y, value in enumerate(line, 0):
            line_values = line_values + " " + get_marble_character(value) + " "
        print(" " + str(x + 1) + " | " + line_values + "|")
    print("   └───────────────────┘\n")
