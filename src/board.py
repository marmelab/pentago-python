from copy import deepcopy
from constant import BOARD_SIZE
import numpy as np


def construct_board():
    return np.array([[0] * BOARD_SIZE for _ in range(BOARD_SIZE)], int)


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

        if is_board_full(board):
            return None

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

        r = range(0, BOARD_SIZE)

        # If position is outside boundaries or on an already filled position.
        if x not in r or y not in r or board[x, y] != 0:
            return None

        # Return 2 dim array relative position (e.g (0, 0))
        return (x, y)
    except:
        return None


def add_marble_to_board(board, user_value):
    # Detect if user_value is a valid coords for our board.
    position = get_position_if_valid(board, user_value)

    # If no, raise exception
    if position == None:
        raise ValueError("Position given is not correct")

    # Else, return board with new added value
    board = deepcopy(board)
    board[position] = 1
    return board


"""
get_quarter_boundaries_from_rotation_key get an integer and return tuple of slices for a 2d range.

rotation_key: int 1 to 8
Each quarter has 2 possibilites of rotation (counter clockwise & clockwise) :

      2 ↻  3 ↺
 1 ↺ ┌───+───┐  4 ↻
     | 1 | 2 |
     |───+───|
     | 4 | 3 |
 8 ↻ └───+───┘ 5 ↺
      7 ↺  6 ↻ 

get_quarter_boundaries_from_rotation_key(2) should return (slice(0, 3), slice(3, 6)) because 3 // 2 = 1.

By querying this tuple of slices in a NumPy array we should be able to get a sub-view of this array.
In this case get a 3*3 array with the 3 first rows and 3 last columns, corresponding to the quarter 2 in the schema above.

Warning: in slice(X, Y), X is included but Y is excluded.

"""


def get_quarter_boundaries_from_rotation_key(rotation_key):
    return {
        0: (slice(0, 3), slice(0, 3)),
        1: (slice(0, 3), slice(3, 6)),
        2: (slice(3, 6), slice(3, 6)),
        3: (slice(3, 6), slice(0, 3))
    }[rotation_key // 2]


def rotate_quarter_of_board(board, user_value):
    try:
        # Trying to convert the given string to an integer.
        rotation_key = int(user_value)

    except:
        raise ValueError("Rotation given is not correct")

    if rotation_key < 1 or rotation_key > 8:
        raise ValueError("Rotation given is not correct")

    # Accept integer between 1 and 8

    # even keys are counter-clockwise, odd are clockwise
    if rotation_key % 2 == 0:
        direction = -1
    else:
        direction = 1

    board = deepcopy(board)

    """
        Get a tuple of slices from the board by using rotation_key.
        slices will contain (slice(x1, y1), slice(x2, y2)) to be able to extract a quarter from the board.
        
        Schema of the board with quarters and rotation keys :
            2 ↻  3 ↺
        1 ↺ ┌───+───┐  4 ↻
            | 1 | 2 |
            |───+───|
            | 4 | 3 |
        8 ↻ └───+───┘ 5 ↺
            7 ↺  6 ↻ 
        rotation_key = 3 ↺
        get_quarter_boundaries_from_rotation_key(3 - 1) will return 2 dimensions slices corresponding to the quarter 2.

    """
    slices = get_quarter_boundaries_from_rotation_key(rotation_key - 1)

    """
        Extract a quarter from the board by giving tuple of slices.
        NumPy array allow us to get parts (slice) of an array of 2 dimensions : "arr[(slice(x1, y1), slice(x2, y2))]"
        which correspond to a sub-view.
        We get the quarter 2 of the board if we querying board[(slice(0, 3), slice(3, 6))].
        +───┐
        | 2 |
        +───|
    """
    quarter = board[slices]

    """
        np.rot90 rotate a 2d array by 90 degrees
        in clockwise (direction = -1) or counter clockwise (direction = 1).
      
        np.rot90(quarter, -1) will result :
        +───┐      +───┐
        |👆 | ===> | 👉|
        +───|      +───|
    """
    rotated_quarter = np.rot90(quarter, direction)

    """
        Finally, board[slices] will be updated with the rotated quarter.
         ┌───+───┐
         | 1 | 👉|
         |───+───|
         | 4 | 3 |
         └───+───┘

    """
    board[slices] = rotated_quarter

    return board
